/*
  Prueba Léxica Conjunta
  Valida los aportes de Sofía Izaguirre y Daniel Cortez
*/

void main() {
  // 1. Tipos de datos, variables y constantes (Sofía y Daniel)
  int edadMascota = 5;
  double peso = 12.5;
  bool estaVacunado = true;
  var enTratamiento = false;
  
  final int idConsulta = 1024;
  const double costoBase = 15.0;

  Map registroClinico;
  Set vacunasAplicadas;

  // 2. Manejo de nulos (Daniel) y Asignación (Sofía)
  int? proximaCita; 

  // 3. Estructuras de control (Sofía) y Operadores (Daniel)
  if (edadMascota >= 5 && peso != 0.0) {
    print(true);
  } else {
    print(false);
  }

  while (peso < 20.0 || !estaVacunado) {
    break;
  }

  for (int i = 0; i <= 3; i = i + 1) {
    // Revisión de rutina
  }

  switch (idConsulta) {
    // Selección de casos
  }

  // 4. Operador Flecha (Daniel) y retorno (Sofía)
  int calcularDosis() => 2;
  
  return;
}