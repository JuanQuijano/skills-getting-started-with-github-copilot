// Calculadora Simple de Consola
using System;

namespace CalculadoraConsola
{
    class Program
    {
        static void Main(string[] args)
        {
            bool continuar = true;
            
            Console.WriteLine("=================================");
            Console.WriteLine("  Calculadora Simple de Consola");
            Console.WriteLine("=================================\n");
            
            while (continuar)
            {
                try
                {
                    // Solicitar primer número
                    Console.Write("Ingrese el primer número: ");
                    double numero1 = Convert.ToDouble(Console.ReadLine());
                    
                    // Solicitar operación
                    Console.Write("Ingrese la operación (+, -, *, /): ");
                    string? operacion = Console.ReadLine();
                    
                    // Solicitar segundo número
                    Console.Write("Ingrese el segundo número: ");
                    double numero2 = Convert.ToDouble(Console.ReadLine());
                    
                    double resultado = 0;
                    bool operacionValida = true;
                    
                    // Realizar la operación
                    switch (operacion)
                    {
                        case "+":
                            resultado = numero1 + numero2;
                            break;
                        case "-":
                            resultado = numero1 - numero2;
                            break;
                        case "*":
                            resultado = numero1 * numero2;
                            break;
                        case "/":
                            if (numero2 == 0)
                            {
                                Console.WriteLine("\nError: No se puede dividir entre cero.");
                                operacionValida = false;
                            }
                            else
                            {
                                resultado = numero1 / numero2;
                            }
                            break;
                        default:
                            Console.WriteLine("\nOperación no válida. Use +, -, * o /");
                            operacionValida = false;
                            break;
                    }
                    
                    // Mostrar resultado
                    if (operacionValida)
                    {
                        Console.WriteLine($"\nResultado: {numero1} {operacion} {numero2} = {resultado}");
                    }
                }
                catch (FormatException)
                {
                    Console.WriteLine("\nError: Por favor ingrese un número válido.");
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"\nError: {ex.Message}");
                }
                
                // Preguntar si desea continuar
                Console.Write("\n¿Desea realizar otra operación? (s/n): ");
                string? respuesta = Console.ReadLine()?.ToLower();
                continuar = (respuesta == "s" || respuesta == "si" || respuesta == "sí");
                
                if (continuar)
                {
                    Console.WriteLine();
                }
            }
            
            Console.WriteLine("\n¡Gracias por usar la calculadora!");
        }
    }
}
