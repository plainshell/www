# www.plainshell.com

Przybyszu z krainu shella, dziś już możesz uruchomić dowolny skrypt z pliku readme selektywnie

## TODO

w planach jest:
+ skanowanie struktury plików i pokazywanie w menu wszystkich skryptów w plikach w danej ścieżce
+ utworzenie jednego menu, gdzie możesz sobie wybrać co chcesz uruchomić, co jest przydatne w kontekście wielu projektów w różnych folderach


## Nagłówki

skrypt python, który jest obsługiwany z linii polceceń shellu, czytający przykładowy plik README.md w formacie markdown i wyświetlający menu pomocy z pliku markdown listując nagłówki header. Po wybraniu z menu polecenia skrypt powinien uruchomić  zawartość, która jest kodem znajdująca się w separatorach ``` w zależności od języka programowania powinna doinstalować pakiety potrzebne do uruchomienia bazując na systemie linux.
Skrypt musi być uruchamiany za pomocą praw uprawnionych do instalowania pakietów. Dla skryptów pythonowych, muszą być zainstalowane pakiety markdown i PyYAML. Może to zająć minuty, aby skrypt zaczęło poprawnie działać.

Skrypt wymaga dosyć skomplikowanej logiki i znajomości różnych języków programowania. Poniżej znajduje się przykładowy kod, który może służyć jako punkt wyjścia. Dalsze dostosowanie i rozszerzenie kodu może obejmować wydajne parsowanie i wykonywanie kodu napisanego w różnych językach programowania z instalacją odpowiednich zależności.

Możesz uruchomić polecenie w terminalu `python3 plainshell.py opcja` , 
gdzie opcja to numer nagłówka, którego zawartość (kod) chcesz uruchomić. 
Bez opcji, skrypt wyświetli menu pomocy listując nagłówki. 

```bash
./plainshell.sh
```

## separatory

skrypt python, który jest obsługiwany z linii polceceń shellu, czytający przykładowy plik README.md w formacie markdown i wyświetlający menu pomocy z pliku markdown listując zawartość, która jest kodem znajdująca się w separatorach ``` w zależności od języka programowania powinna doinstalować pakiety potrzebne do uruchomienia zawartości bazując na systemie linux. Wybieranie skryptu z menu powinno być możliwe za pomocą kolejnej liczby  odzwierciedlającej kolejny skrypt w pliku README.md
Skrypt musi być uruchamiany za pomocą praw uprawnionych do instalowania pakietów. Dla skryptów pythonowych, muszą być zainstalowane pakiety markdown i PyYAML. 


```bash
./plainshell.sh
```

## python

```bash
python3 --version
```

---
+ [edit](https://github.com/plainshell/www/edit/main/README.md)
