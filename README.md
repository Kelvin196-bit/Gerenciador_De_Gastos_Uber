# 📊 Uber Gasto Tracker – Projeto Pessoal em Python

Este foi meu **primeiro projeto pessoal solo em Python**, desenvolvido durante minha graduação no curso de **Bacharelado em Matemática na UFC** na cadeira de fundamentos de programação. Criei essa aplicação com o objetivo de gerenciar e calcular meus gastos, lucros e rendimentos enquanto trabalhava como motorista da Uber.

Todo o projeto foi desenvolvido diretamente no celular usando o aplicativo Pydroid 3, o que o torna acessível para quem quer programar sem um computador.

O funcionamento é simples: você insere os dados de cada corrida (quilometragem, valor recebido, valor da gasolina) e o programa realiza os cálculos automaticamente. Os resultados são salvos localmente em arquivos **.txt** e também **enviados automaticamente para o GitHub** como **Gists privados**, servindo como backup remoto.

---

## 🚀 Funcionalidades

- Calcula:
  - Consumo de combustível.
  - Lucro líquido.
  - Rendimento proporcional.
  - Margem de lucro por dupla.
- Armazena os dados em três arquivos de texto:
  - lucro.txt: Lucro por corrida.
  - Rendimentos.txt: Rendimento proporcional.
  - margem_de_lucro_percentual.txt: Margem de lucro (caso de divisão de lucros).
- Salva os dados com data e hora da corrida.
- Envia os arquivos automaticamente como **Gists privados no GitHub**.
- Executável diretamente pelo celular usando **Pydroid 3**.

Cada vez que você roda o código e preenche os dados da corrida, ele:

1. Calcula os resultados.
2. Atualiza os arquivos locais.
3. Envia automaticamente esses arquivos para o GitHub, criando (ou atualizando) Gists privados com os mesmos dados.

---

## 📲 Desenvolvido com: Pydroid 3 (Android)

Este projeto foi totalmente feito no app **Pydroid 3** para Android, que permite escrever, testar e rodar código Python direto do celular.

Você pode baixar o app gratuitamente na Google Play Store:  
🔗 https://play.google.com/store/apps/details?id=ru.iiec.pydroid3

---

## 🧩 Tecnologias e dependências

- **Python 3 (via Pydroid 3)**
- Biblioteca externa necessária: requests (para envio ao GitHub)

## 📦 Como instalar dependências no Pydroid 3:

1. Abra o **Pydroid 3**.
2. Toque em Terminal.
3. Digite o seguinte comando no terminal:
   pip install requests
4. Aguarde o download e a instalação da biblioteca.

---

## 🔐 Como obter e configurar o token do GitHub

Para que o script possa enviar os dados para o seu GitHub como **Gists privados**, você precisa gerar um **Token de Acesso Pessoal** com permissão adequada.

### ▶️ Passo a passo:

1. Acesse: [https://github.com/settings/tokens](https://github.com/settings/tokens)
2. Clique em **"Generate new token (classic)"**
3. Dê um nome e marque a opção:
- ✅ gist
4. Clique em **"Generate token"**
5. Copie o token gerado e cole no seu código na linha onde está:
  
token = "INSIRA_SEU_TOKEN_AQUI"

❗ Nunca compartilhe esse token publicamente. Recomendável usar função os.getenv().


## 🧪 Como usar
1. Execute o script no Pydroid 3.
2. Digite os valores solicitados (km inicial, km final, valor da Uber, preço da gasolina).
3. O script fará os cálculos e exibirá os resultados na tela.
4. Os resultados são salvos em arquivos .txt e enviados para seu GitHub.

### 📘 Exemplo de entrada

Digite o quilômetro inicial: 1000
Digite o quilômetro final: 1050
Digite quanto você recebeu da Uber: 80
Digite o valor da gasolina: 6.19

###  🧾 Exemplo de saída

Você consumiu 1.09 Litros
Você gastou R$ 6.75
Você tem que enviar para Kelv: R$ 45.37
Você lucrou: R$ 34.87
Seu rendimento foi: 3.47
Seu lucro real: R$ 33.12
Sua margem de lucro (por dupla) é: 41.4%

###  📁 Estrutura do Projeto

uber-gasto-tracker/
├── lucro.txt
├── Rendimentos.txt
├── margem_de_lucro_percentual.txt
├── main.py       ← Arquivo principal do código
└── README.md     ← Este arquivo

## 📌 Autor
Desenvolvido por Kelv Alves de Freitas
👨‍🎓 estudante de Matemática (UFC)
🚗 Motorista da Uber & Programador iniciante














