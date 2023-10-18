class Genotype {
  late final String _genotype;

  Genotype(String genotype) {
    if (correctGenotype(genotype)) {
      _genotype = genotype;
    } else {
      throw ArgumentError("invalido $genotype");
    }
  }

  @override
  String toString() {
    if (_genotype.isNotEmpty) {
      return _genotype;
    } else {
      return _genotype.toString();
    }
  }

  bool correctGenotype(String genotype) {
    final allGenotypes = ["AA", "Ai", "BB", "Bi", "AB", "ii"];
    return allGenotypes.contains(genotype);
  }   
  

  String? get bloodType {
    if (["AA", "Ai"].contains(_genotype)) {
      return "A";
    } else if (["BB", "Bi"].contains(_genotype)) {
      return "B";
    } else if (_genotype == "ii") {
      return "O";
    } else if (_genotype == "AB") {
      return "AB";
    }
  }

  List<String> get alelles {
    List<String> lista = [];
    if (!["AA", "BB", "ii"].contains(_genotype)) {
      for (int i = 0; i < _genotype.length; i++) {
        lista.add(_genotype[i]);
      }
    } else {
      lista.add(_genotype[0]);
    }
    return lista;
  }
  List<String> get agglutinogens {
    List<String> lista2 = [];
    if (["AA", "Ai"].contains(_genotype)) {
      lista2.add('A');
    } else if (["BB", "Bi"].contains(_genotype)) {
      lista2.add('B');
    } else if (_genotype == "AB") {
      lista2.add('A');
      lista2.add('B');
    }
    return lista2;
  }

  List<String> get agglutinins {
    List<String> agglutinins = [];
    if (["AA", "Ai"].contains(_genotype)) {
      agglutinins.add('B');
    } else if (["BB", "Bi"].contains(_genotype)) {
      agglutinins.add('A');
    } else if (_genotype == "ii") {
      agglutinins.add('A');
      agglutinins.add('B');
    }
    return agglutinins;
  }




  List<String> offsprings(Genotype other) {
    List<String> offspringSet = [];
    for (var alelo1 in _genotype.split('')) {
      for (var alelo2 in other._genotype.split('')) {
            String um = alelo1 + alelo2;
            if (um == 'iA') {
              um = 'Ai';
            } else if (um == 'iB') {
              um = 'Bi';
            } else if (um == 'BA') {
              um = 'AB';
            }
            if (!offspringSet.contains(um)) {
              offspringSet.add(um);
            } 
          }
          return offspringSet;
        }
  }

  bool compatible(Genotype genotypex) {
    if (_genotype == 'AB' && genotypex._genotype != 'AB') {
      return true;
    } else if (_genotype == 'ii') {
      return true;
    } else if (_genotype[0].contains(genotypex._genotype)) {
      return true;
    } else {
      return false;
    }
  }
}
