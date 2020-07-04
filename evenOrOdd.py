#!/usr/bin/python3
import os


def evenOrOdd(number):
    if (number % 2) == 0:
        result = ('O numero {} e PAR!'.format(number))
    else:
        result = ('O numero {} e IMPAR!'.format(number))
    return result


QUERY = os.getenv('QUERY_STRING')
number = int(QUERY.split('=')[1])
result = evenOrOdd(number)


print('Content-type:text/html\r\n\r\n')
print('<!DOCTYPE html>')
print('<html lang="pt-BR">')
print('  <head>')
print('    <meta charset="UTF-8" />')
print('    <meta name="viewport" content="width=device-width, initial-scale=1.0" />')
print('    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">')
print('    <style>')
print('      * {')
print('        margin: 0;')
print('        padding: 0;')
print('        outline: 0;')
print('        box-sizing: border-box;')
print('        font-family: Roboto, sans-serif;')
print('      }')
print('      body {')
print('        background: #f0f0f5;')
print('        -webkit-font-smoothing: antialiased;')
print('        text-align: center;')
print('        margin-top: 25vh;')
print('      }')
print('      h1 {')
print('        font-size: 48px;')
print('        margin-bottom: 16px;')
print('        margin-top: 16px;')
print('      }')
print('      p {')
print('        margin-bottom: 8px;')
print('      }')
print('      form {')
print('        display: flex;')
print('        align-items: center;')
print('        justify-content: center;')
print('      }')
print('      input {')
print('        width: 300px;')
print('        font-size: 18px;')
print('        padding: 8px;')
print('        border: 2px solid #24a0ed;')
print('        margin-right: 2px;')
print('      }')
print('      button {')
print('        cursor: pointer;')
print('        width: 80px;')
print('        background: #24a0ed;')
print('        color: white;')
print('        border: 0;')
print('      }')
print('      input, button {')
print('        height: 40px;')
print('      }')
print('    </style>')
print('    <title>Par ou Impar?</title>')
print('  </head>')
print('  <body>')
print('    <h1>Par ou Impar?</h1>')
print('    <p>')
print('      Digite um numero inteiro, e descubra se ele e <strong>par</strong> ou')
print('      <strong>impar</strong>!')
print('    </p>')
print('    <form action="/cgi-bin/evenOrOdd.py" method="GET">')
print('      <input')
print('        type="number"')
print('        name="number"')
print('        placeholder="Digite um numero inteiro"')
print('      />')
print('      <button type="submit">Verificar</button>')
print('    </form>')
print('    <h1><strong>{}</strong></h1>'.format(result))
print('  </body>')
print('</html>')
