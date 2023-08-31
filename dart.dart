import 'dart:io';

void main() {
  print('***Exibe os N primeiros naturais ímpares***');
  stdout.write('Informe N: ');
  var data = stdin.readLineSync();
  var counter = int.parse(data ?? '0');
  var oddNumber = 1;
  stdout.write('\n' + 'Os $counter primeiros naturais impares são: ');
  while (counter > 0) {
    stdout.write('$oddNumber ');
    oddNumber += 2;
    counter -= 1;
    //stdout.write('\n');
  }
}
