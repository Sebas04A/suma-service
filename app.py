from spyne import Application, rpc, ServiceBase, Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class SumaService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def sumar(ctx, a, b):
        return a + b

app = Application(
    [SumaService],
    tns='mi.calculadora.suma',
    in_protocol=Soap11(),
    out_protocol=Soap11()
)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    print("Servicio de Suma corriendo en http://localhost:8000")
    server = make_server('0.0.0.0', 8000, WsgiApplication(app))
    server.serve_forever()
