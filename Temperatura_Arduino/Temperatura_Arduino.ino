// Programa : Leitor temperatura sensores DS18B20
// Alterações : Arduino e Cia
// Este programa usa o endereço físico de cada sensor para mostrar as 
// informações de temperatura no Serial Monitor

#include <OneWire.h>

#include <DallasTemperature.h>

// Conectar o pino central dos sensores ao pino 10 do Arduino
#define ONE_WIRE_BUS 10

// Setup a oneWire instance to communicate with any OneWire devices
OneWire oneWire(ONE_WIRE_BUS);

// Pass our oneWire reference to Dallas Temperature. 
DallasTemperature sensors(&oneWire);
DeviceAddress thermometerOne = { 0x28, 0xFF, 0x72, 0xC0, 0x62, 0x15, 0x01, 0x38 };
DeviceAddress thermometerTwo = { 0x28, 0xFF, 0xFA, 0x65, 0x72, 0x15, 0x02, 0x4D };

void setup(void)
{
  // start serial port
  Serial.begin(9600);
  // Start up the library
  sensors.begin();
  // set the resolution to 10 bit (good enough?)
  sensors.setResolution(thermometerOne, 10);
  sensors.setResolution(thermometerTwo, 10);
}

void getTemp(){
  printTemperature(thermometerOne);
  Serial.print(" ");
  printTemperature(thermometerTwo);
}

void printTemperature(DeviceAddress deviceAddress)
{ 
  sensors.requestTemperatures();
  float tempC = sensors.getTempC(deviceAddress);
  if (tempC == -127.00) 
  {
    Serial.print("Erro ao ler temperatura !");
  } 
  else 
  {
    Serial.print(tempC);
  }
}

void IDFuncao(String funcao){
 if (funcao == String("temp")){
  getTemp(); 
 }
}

void decodificaMensagem(String mensagem){
  int i;
  String funcao = "";
  for (i=1; i<=4; i++){
    funcao = funcao + String(mensagem[i]);
  }
  IDFuncao(funcao);
}

void loop(void)
{ 
  //Verificando se tem algo na Porta
  if (Serial.available() > 0){
    String mensagem = Serial.readString();
    String inicio = String(mensagem[0]);
    
    //Verificando se o que eu recebi começa com #
    if (inicio == String("#")){
      decodificaMensagem(mensagem);
    }
  }
}
