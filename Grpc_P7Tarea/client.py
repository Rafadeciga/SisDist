import grpc
import shop_pb2
import shop_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = shop_pb2_grpc.ShopServiceStub(channel)
        
        # Ejemplo de llamada al método GetProductInfo
        product_id = "123"
        product_info_request = shop_pb2.ProductInfoRequest(product_id=product_id)
        product_info_response = stub.GetProductInfo(product_info_request)
        if product_info_response.name:
            print(f"Información del Producto {product_id}:")
            print("Nombre:", product_info_response.name)
            print("Descripción:", product_info_response.description)
            print("Precio:", product_info_response.price)
        else:
            print(f"Producto con ID {product_id} no encontrado")

if __name__ == '__main__':
    run()

