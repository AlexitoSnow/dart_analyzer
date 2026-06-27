// Prueba Sintáctica - Desarrollador 1 (Sofia Izaguirre)

int calcularArea(int base, int altura) {
  return base;
}

int funcionVacia() {
}

void main() {
  var saludo = "Hola, evaluador";
  var contador = 0;

  Map<String, int> edades = {'Juan': 25, 'Ana': 30};
  Map<String, double>? mapaNulable;
  Map diccionarioVacio = {};

  // ERROR SINTÁCTICO INTENCIONAL 1: Falta la coma (,) separando los elementos del mapa
  // El analizador arrojará error cerca de 'Maria'
  Map<String, int> mapaError = {'Juan': 25 'Maria': 30};

  var edad = 20;
  var tienePermiso = true;

  if (edad >= 18 && tienePermiso == true) {
    var acceso = true;
  } else {
    var acceso = false;
  }

  // ERROR SINTÁCTICO INTENCIONAL 2: Operador relacional incompleto (falta un número después del >=)
  // El analizador arrojará error cerca del ')'
  if (edad >= ) {
    var denegado = true;
  }
}