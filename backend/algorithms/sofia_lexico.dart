/**
 * Prueba de código para Sofía Izaguirre
 * Snippet de prueba para las reglas y tokens de Sofía Izaguirre
 * (int, Map, var, final, const, true, false, if, else, for, while, return, 
 * print, switch, break, void, ID, asignación y enteros).
*/
void main() {
  var x = 10;
  final int constanteEntera = 42;
  const bool esVerdad = true;
  bool esFalso = false;
  Map<String, int>? miMapa;
  
  if (esVerdad) {
    print(x);
  } else {
    print(0);
  }
  
  for (int i = 0; i < 5; i = i + 1) {
    while (x > 0) {
      break;
    }
  }
  
  switch (x) {
    // vacio
  }
  
  return;
}
