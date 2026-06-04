planos=  {
    "prata":200,
    "ouro":300,
    "diamante":400,
    "esmeralda":500
}
total=0

def identificar(cpf,cpf_cliente):
       if cpf == cpf_cliente:
        return True
       return False
def calculo(idade,sexo,plano_nome,dependentes):
         idade = int(idade) 
         valor_plano = planos.get(plano_nome.lower(), 0)
        
    
         if idade<13:

           desconto=valor_plano*0.30
           total=valor_plano-desconto
           print(f"o valor do seu plano sera de{total}")

         elif idade>=60:

           extra=valor_plano*0.40
           total=valor_plano+extra
           print(f"o valor total do seu plano  sera{total}")

         elif idade>=13 and idade<35 and  sexo=="feminino":#ver oque o baiano colocou    

          extra=valor_plano*0.30
          total=valor_plano+extra
          print(f"o valor do seu plano sera:{total}")

         else:
          total=valor_plano
          print(total)

         if len(dependentes)>1: 
          
          
          desconto_dependentes=total*0.20
          total-=desconto_dependentes
          print(f"total com o desconto dos dependentes:{total}")
         return total