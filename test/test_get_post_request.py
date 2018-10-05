import json
import threading
import urllib.request


class SendOrderEvent(threading.Thread):
    def run(self):
        body = {'id': "5623859", 'Estado': 'LIQUIDACION', 'Detalle': '0'}
        url = "http://localhost:3000/orden_events"
        response = send_post(url, body)
        assert response.code == 200


class SendOrder(threading.Thread):
    def run(self):
        body = dict(
            Clave=2456303,
            FechaOperacion=20180618,
            InstitucionOrdenante=846,
            InstitucionBeneficiaria=90646,
            ClaveRastreo="PRUEBATAMIZI1",
            Monto=100.0,
            NombreOrdenante="BANCO",
            TipoCuentaOrdenante=40,
            CuentaOrdenante="846180000500000008",
            RFCCurpOrdenante="ND",
            NombreBeneficiario="TAMIZI",
            TipoCuentaBeneficiario=40,
            CuentaBeneficiario="646180157000000004",
            RFCCurpBeneficiario="ND",
            ConceptoPago="PRUEBA",
            ReferenciaNumerica=2423,
            Empresa="TAMIZI"
        )
        url = "http://localhost:3000/orden_events"
        response = send_post(url, body)
        assert response.code == 201


def send_post(url, body):
    req = urllib.request.Request(url)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    json_data = json.dumps(body)
    json_data_as_bytes = json_data.encode('utf-8')
    req.add_header('Content-Length', len(json_data_as_bytes))
    response = urllib.request.urlopen(req, json_data_as_bytes)
    return response


class TestGetPostRequests:

    def test_multiple_request(self):

        threads = []
        for r in range(30):
            t = SendOrderEvent()
            t.start()
            threads.append(t)

        for r in threads:
            r.join()

    def test_multiple_order(self):
        threads = []
        for r in range(30):
            t = SendOrder()
            t.start()
            threads.append(t)

        for r in threads:
            r.join()

    def test_ping(self):
        res = send_post('http://localhost:3000/', None)
        assert res.status_code == 200