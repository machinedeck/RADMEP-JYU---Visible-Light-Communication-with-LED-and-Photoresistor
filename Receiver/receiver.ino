// Code from: https://www.youtube.com/watch?v=IdU6eCJ9Rh0
// Alternatively: https://github.com/SaadOjo/DIY_Li-Fi/blob/master/receiver/receiver.ino
// Also: https://pastebin.com/rkPgrv92

#define Period 1500
#define Threshold 512
#define Threshold2 358
#define Output A1
#define Out A2

void setup() {
  Serial.begin(57600);
  
}

void loop() {

  int vo = analogRead(Out);
 
  if (vo > Threshold2)
  {
  
    Serial.println(get_byte());
 
  }
  
}


int get_byte()
{
  int array[8];
  char binaryString[9];
  // unsigned 
  // char ret = 0;
  // int myarray[8];
  // int totals = 0;
  // int new = 0;
  delay(1500 + Period * 0.5);
  for (int i = 0; i < 8; i++)
  {
   
    int value = bit_value();
    // totals += (value * pow(2, i));
    array[i] = value * pow(2, i);
    binaryString[i] = value + '0';
   
    delay(Period);
  }
  binaryString[8] = '\0';
  // Serial.print
  // return myarray;
  // sprintf(myarray)
  // return ret;

  // int tot = 0;
  // for (int i = 0; i < 8; i++)
  // {
  //   tot += array[i];
  // }
  // return tot;
  int number = strtol(binaryString, NULL, 2);

  return number;
}

int bit_value()
{
int voltage = analogRead(Output);
    if (voltage > Threshold)
    {
      int value = 1;
      return value;
    }
    else {
      int value = 0;
      return value;
    }
}







// unsigned char get_byte()
// {
//   unsigned char ret = 0;
//   delay(1000 + Period * 0.5);
//   for (int i = 0; i < 8; i++)
//   {
//     ret = ret | get_gain() << i;
//     // Serial.println(ret)
//     delay(Period);
//   }
//   return ret;
// }
// void print_byte(unsigned char my_byte)
// {
//   char buff[2];
//   sprintf(buff, "%c", my_byte);
//   Serial.print(buff);
// }