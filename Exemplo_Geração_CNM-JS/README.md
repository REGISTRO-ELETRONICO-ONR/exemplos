# Gerador de CNM (JS)

## Descrição
O `cnmGenerator` é uma função que gera um número CNM com dígito verificador a partir de um CNS e um número de registro.

A função utiliza a biblioteca `cdigit` para calcular o dígito verificador do número CNM. Certifique-se de que a biblioteca `cdigit` esteja instalada no ambiente de execução antes de utilizar esta função.

## Parâmetros
- `cns` (string): O número do CNS a ser utilizado para gerar o número CNM.
- `number` (string): O número de registro a ser utilizado para gerar o número CNM. Este número deve ter no máximo 7 dígitos.

## Retorno
A função retorna uma string contendo o número CNM formatado no seguinte padrão: "CNS.BOOK.NUMBER-DIGIT", onde:
- `CNS` é o número do CNS fornecido como parâmetro.
- `BOOK` é o valor fixo "2" (representando o tipo de livro associado ao número CNM).
- `NUMBER` é o número de matrícula fornecido como parâmetro.
- `DIGIT` é o dígito verificador calculado pela função.

## Exemplo de Uso
```javascript
import * as cdigit from "cdigit";

const cns = "999999";
const number = "0000001";

const result = cnmGenerator(cns, number);
console.log(result);
```


Saída:

999999.2.0000001-XX


Neste exemplo, o número CNM é gerado a partir do CNS "999999" e do número de registro "0000001". O resultado é exibido no console com o dígito verificador substituído por "XX" para simplificar o exemplo.

## Dependências
Certifique-se de ter a biblioteca `cdigit` instalada antes de utilizar esta função. Caso ainda não tenha instalado, você pode instalá-la utilizando o seguinte comando:

`npm install`


## Limitações
- O número de registro fornecido deve ter no máximo 7 dígitos.
- Certifique-se de que o CNS fornecido seja válido e esteja no formato correto.
- A função depende da biblioteca `cdigit` para calcular o dígito verificador. Certifique-se de tê-la instalada e importada corretamente.
