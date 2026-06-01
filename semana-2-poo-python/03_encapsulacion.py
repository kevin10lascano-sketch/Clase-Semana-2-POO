"""
Semana 2 - Programación Orientada a Objetos
Tema: Encapsulación

La encapsulación permite proteger los datos internos de un objeto
y controlar su acceso mediante métodos.
"""


class CuentaBancaria:
    """
    Esta clase representa una cuenta bancaria.

    El atributo _saldo se considera interno.
    Por convención, no debería modificarse directamente
    desde fuera de la clase.
    """

    def __init__(self, saldo=0):
        self._saldo = saldo

    def depositar(self, monto):
        """
        Permite depositar dinero si el monto es válido.
        """
        if monto > 0:
            self._saldo += monto
            print(f"Depósito realizado: ${monto}")
        else:
            print("El monto a depositar debe ser mayor que cero.")

    def retirar(self, monto):
        """
        Permite retirar dinero si el monto es válido
        y si existe saldo suficiente.
        """
        if 0 < monto <= self._saldo:
            self._saldo -= monto
            print(f"Retiro realizado: ${monto}")
        else:
            print("No se puede realizar el retiro.")

    def obtener_saldo(self):
        """
        Permite consultar el saldo de forma controlada.
        """
        return self._saldo


# Creación de una cuenta con saldo inicial
cuenta = CuentaBancaria(100)

# Operaciones controladas mediante métodos
cuenta.depositar(50)
cuenta.retirar(30)

# Consulta del saldo mediante un método
print(f"Saldo actual: ${cuenta.obtener_saldo()}")