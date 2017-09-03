from unittest import TestCase
from unittest.mock import call, Mock, patch, MagicMock, PropertyMock
from hashlib import md5
from datetime import date
from flask import session
from datetime import datetime
from io import StringIO, BytesIO
from bson.binary import Binary

import json

import db
import req_handler
from req_handler import flask_app


class ReqHandlerTest(TestCase):
    def setUp(self):
        self.app = flask_app.test_client()

        with self.app.session_transaction() as session:
            session["locale"] = "en"

    def tearDown(self):
        pass

    # --------------------------------------------------------------------
    def do_request(self, name, email, source_lang, dest_lang, file, phone_number="", comment=""):
        return self.app.post('/request/', data=dict(name=name, email_address=email,
                                                    source_lang=source_lang,
                                                    dest_lang=dest_lang,
                                                    phone_number=phone_number, comment=comment, file=file),
                             follow_redirects=True)

    @patch("sendmail.send")
    @patch("db.Request")
    def test_request_handler_must_store_valid_data_into_db_and_return_ok(self, RequestMock, send_mail_mock):
        req_mock = MagicMock()
        RequestMock.return_value = req_mock

        name = "Angela Devis"
        email = "angela.devis@example.com"
        source_lang = db.ENGLISH
        dest_lang = db.RUSSIAN
        phone_number = "+5(123)1234567"
        comment = "Whatever"
        filename = "asdf.doc"
        file_content = b"hi everyone"
        file = (BytesIO(file_content), filename)

        resp = self.do_request(name, email, source_lang, dest_lang, file, phone_number, comment)

        req_mock.save.assert_called_with()
        req_mock.__setitem__.assert_any_call("name", name)
        req_mock.__setitem__.assert_any_call("email", email)
        req_mock.__setitem__.assert_any_call("source_lang", source_lang)
        req_mock.__setitem__.assert_any_call("dest_lang", dest_lang)
        req_mock.__setitem__.assert_any_call("phone_number", phone_number)
        req_mock.__setitem__.assert_any_call("comment", comment)
        req_mock.__setitem__.assert_any_call("name", name)
        req_mock.__setitem__.assert_any_call("file_name", filename)
        req_mock.__setitem__.assert_any_call("file", Binary(file_content))

        assert resp.status_code == 200

    # --------------------------------------------------------------------
    @patch("sendmail.send")
    @patch("db.Request")
    def test_request_handler_must_NOT_store_data_into_db_if_invalid_file_and_return_400_bad_request(self, RequestMock, send_mail_mock):
        req_mock = MagicMock()
        RequestMock.return_value = req_mock

        name = "Angela Devis"
        email = "angela.devis@example.com"
        source_lang = db.ENGLISH
        dest_lang = db.RUSSIAN
        phone_number = "+5(123)1234567"
        comment = "Whatever"
        filename = "asdf.docc"
        file_content = b"hi everyone"
        file = (BytesIO(file_content), filename)

        resp = self.do_request(name, email, source_lang, dest_lang, file, phone_number, comment)

        assert not req_mock.save.called
        assert resp.status_code == 400

    # --------------------------------------------------------------------
    @patch("sendmail.send")
    @patch("db.Request")
    def test_request_handler_must_NOT_store_data_into_db_if_same_lang_and_return_400_bad_request(self, RequestMock, send_mail_mock):
        req_mock = MagicMock()
        RequestMock.return_value = req_mock

        name = "Angela Devis"
        email = "angela.devis@example.com"
        source_lang = db.ENGLISH
        dest_lang = db.ENGLISH
        phone_number = "+5(123)1234567"
        comment = "Whatever"
        filename = "asdf.doc"
        file_content = b"hi everyone"
        file = (BytesIO(file_content), filename)

        resp = self.do_request(name, email, source_lang, dest_lang, file, phone_number, comment)

        assert not req_mock.save.called, 'save() was called and should not have been'
        assert resp.status_code == 400

    # --------------------------------------------------------------------
    def test_must_correctly_calculate_chronopay_sign(self):
        resp = self.app.get("/sign/1.00")
        result = json.loads(resp.data.decode())
        assert resp.status_code == 200
        assert result['sign'] == 'cba44b55cff675089347e65b625231ef'
        assert result['amount'] == '1.00'

        resp = self.app.get("/sign/1")
        result = json.loads(resp.data.decode())
        assert resp.status_code == 200
        assert result['sign'] == 'cba44b55cff675089347e65b625231ef'
        assert result['amount'] == '1.00'

        resp = self.app.get("/sign/555")
        result = json.loads(resp.data.decode())
        assert resp.status_code == 200
        assert result['sign'] == '696e0a8fa078a32736e2293048de3df3'
        assert result['amount'] == '555.00'

        resp = self.app.get("/sign/1.")
        result = json.loads(resp.data.decode())
        assert resp.status_code == 200
        assert result['sign'] == 'cba44b55cff675089347e65b625231ef'
        assert result['amount'] == '1.00'

    # --------------------------------------------------------------------
    def test_must_return_http_400_if_amount_is_invalid_or_zero(self):
        resp = self.app.get("/sign/asdf")
        assert resp.status_code == 400

        resp = self.app.get("/sign/433sdf")
        assert resp.status_code == 400

