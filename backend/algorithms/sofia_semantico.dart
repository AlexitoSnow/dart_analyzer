// Prueba Semántica - Desarrollador 1 (Sofia Izaguirre)

void main() {
  const int limite = 100;
  limite = 200; // Error Semántico: No se puede reasignar un valor a la constante 'limite'.

  int resultado = valorNoDeclarado; // Error Semántico: La variable 'valorNoDeclarado' no ha sido declarada antes de su uso.
}
