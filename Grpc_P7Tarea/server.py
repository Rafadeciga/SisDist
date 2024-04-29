import grpc
from concurrent import futures
import shop_pb2
import shop_pb2_grpc

class ShopServicer(shop_pb2_grpc.ShopServiceServicer):
    def PurchaseItem(self, request, context):
        # Lógica para procesar la compra de un artículo
        # Esta es solo una implementación de ejemplo
        total_price = 10 * request.quantity  # Precio unitario de ejemplo
        return shop_pb2.PurchaseResponse(message="Artículo comprado exitosamente", total_price=total_price)

    def MakePayment(self, request, context):
        # Lógica para procesar el pago
        # Esta es solo una implementación de ejemplo
        success = True  # Simulando un pago exitoso
        return shop_pb2.PaymentResponse(message="Pago exitoso", success=success)

    def PlaceOrder(self, request, context):
        # Lógica para realizar un pedido
        # Esta es solo una implementación de ejemplo
        order_id = "123456"  # ID del pedido generado
        purchases = []
        total_price = 0
        for item in request.items:
            total_price += 10 * item.quantity  # Precio unitario de ejemplo
            purchases.append(shop_pb2.PurchaseResponse(message="Artículo comprado exitosamente", total_price=total_price))
        return shop_pb2.OrderResponse(order_id=order_id, purchases=purchases)

    def GetProductInfo(self, request, context):
        # Lógica para obtener información del producto
        # Esta es solo una implementación de ejemplo
        product_info = {
            "123": {"name": "Producto 1", "description": "Descripción del producto 1", "price": 10.0},
            "456": {"name": "Producto 2", "description": "Descripción del producto 2", "price": 20.0},
            "789": {"name": "Producto 3", "description": "Descripción del producto 3", "price": 30.0},
        }
        product_id = request.product_id
        if product_id in product_info:
            info = product_info[product_id]
            return shop_pb2.ProductInfoResponse(name=info["name"], description=info["description"], price=info["price"])
        else:
            context.set_details(f"Producto con ID {product_id} no encontrado")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return shop_pb2.ProductInfoResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    shop_pb2_grpc.add_ShopServiceServicer_to_server(ShopServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor iniciado. Escuchando en el puerto 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

