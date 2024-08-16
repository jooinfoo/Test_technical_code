from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HelloWorldView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"message": "Hello, World!"}, status=status.HTTP_200_OK)

# Create your views here.
class OddNumbersView(APIView):
    def post(self, request, *args, **kwargs):
        input_value = request.data.get('number')

        if input_value is None:
            return Response({"error": "number is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            input_number = int(input_value)
        except ValueError:
            return Response({"error": "number must be an integer"}, status=status.HTTP_400_BAD_REQUEST)

        # Calculate odd numbers
        odd_numbers = [i for i in range(1, input_number + 1) if i % 2 != 0]

        return Response({"odd_numbers": odd_numbers}, status=status.HTTP_200_OK)

class PrimeNumberView(APIView):
    def post(self, request, *args, **kwargs):
        input_value = request.data.get('number')

        if input_value is None:
            return Response({"error": "number is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            number = int(input_value)
        except ValueError:
            return Response({"error": "number must be an integer"}, status=status.HTTP_400_BAD_REQUEST)

        def is_prime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True

        result = is_prime(number)

        return Response({"number": number, "is_prime": result}, status=status.HTTP_200_OK)
      

class StarTriangleView(APIView):
    def post(self, request, *args, **kwargs):
        input_value = request.data.get('number')

        if input_value is None:
            return Response({"error": "number is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            number = str(int(input_value))  # Ensure it's a string of digits
        except ValueError:
            return Response({"error": "number must be an integer"}, status=status.HTTP_400_BAD_REQUEST)

        triangle_pattern = []
        length = len(number)

        for i in range(length):
            digit = int(number[i])
            if digit != 0:
                # Multiply the digit by 10^i to get the correct value, then format with zeros
                line_value = str(digit * (10 ** i))
            else:
                # For zeros, just add the appropriate number of zeros
                line_value = '0' * (i + 2)
            
            # Add the line to the pattern
            triangle_pattern.append(line_value)

        # Join all lines with newline characters
        result = "\n".join(triangle_pattern)

        # Return the result directly as JSON
        return Response({"triangle": result}, status=status.HTTP_200_OK)