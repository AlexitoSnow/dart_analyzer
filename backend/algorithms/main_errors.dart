/**
 * Prueba de código Grupal - main_errors.dart
 * Snippet conjunto con errores intencionales para validación.
 * Contiene errores de los tres tipos: léxicos, sintácticos y semánticos.
 */
void main() {
  var variable = 100;

  // ❌ ERROR SEMÁNTICO INTENCIONAL 1: La sentencia 'break' fuera de bucle/switch.
  break;

  // ❌ ERROR SEMÁNTICO INTENCIONAL 2: Tipo de retorno 'String' no coincide con 'void'.
  return "mismatch";

  // ❌ ERROR SINTÁCTICO INTENCIONAL 1: Falta paréntesis en la condición del if.
  if variable > 50 {
    print("Error");
  }

  // ❌ ERROR SINTÁCTICO INTENCIONAL 2: Función lambda sin valor a retornar.
  bool funcionIncompleta() => ;

  // ❌ ERROR LÉXICO INTENCIONAL 1: El símbolo '~' no pertenece al alfabeto.
  int operacionInvalida = 5 ~ 3;
}

// ❌ ERROR LÉXICO INTENCIONAL 2: '@' no está en el alfabeto.
class MyClass {
  @override
  void test() {}
}
