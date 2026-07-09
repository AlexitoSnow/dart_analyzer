// Prueba Semántica - Desarrollador 3 (Alexander Nieves)

int funcionIncorrecta1() {
  return true; // Error Semántico: El tipo de retorno 'bool' no coincide con el tipo 'int' declarado en la función.
}

void funcionIncorrecta2() {
  break; // Error Semántico: La sentencia 'break' solo puede usarse dentro de un bucle o switch.
}

void main() {
  int x = 10;
  
  for (int i = 0; i < 5; i++) {
    break; // Permitido
  }
}
