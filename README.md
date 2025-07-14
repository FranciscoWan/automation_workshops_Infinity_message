**Automação de Envio de Workshops - INFINITY**
Este é um aplicativo para enviar mensagens automáticas aos grupos de alunos no WhatsApp, lembrando-os sobre os workshops disponíveis para a semana atual e a próxima. O programa foi desenvolvido para facilitar a comunicação com os alunos de forma automatizada.

**Requisitos**
Python 3.x

Bibliotecas necessárias: selenium, json, time, os, webdriver_manager

**Como usar**
1. Preparação
Coloque o executável do programa em uma pasta de sua escolha.

2. Primeira Execução
Na primeira execução, será necessário configurar algumas informações:

Login do Monitor: Insira o CPF (apenas números) e a data de nascimento no formato dd/mm/aa. Esses dados serão salvos para uso futuro, de modo que você não precisará inseri-los novamente, a menos que altere o computador ou deseje mudar a conta do monitor.

Exemplo de entrada:

55544423421
20/06/2003

3. Definir Grupos de WhatsApp
Após o login, será solicitado que você insira os nomes dos grupos de WhatsApp para os quais as mensagens serão enviadas. Você pode pesquisar pelos grupos no WhatsApp e adicionar os nomes desejados.

Insira o nome de um grupo e pressione ENTER.

Repita o processo para adicionar mais grupos.

4. Login no WhatsApp Web
Ao selecionar a opção para enviar mensagens, uma página do Google Chrome será aberta e você precisará fazer login no WhatsApp Web. Após a conclusão do login, aguarde o carregamento do app e, em seguida, retorne ao programa e pressione ENTER para prosseguir.

O programa irá carregar as informações e enviar automaticamente as mensagens para os grupos que você cadastrou.

5. Envio de Workshops
O programa enviará automaticamente as informações dos workshops que ocorrerão nas próximas duas semanas, contando a partir da data de execução do programa.

6. Correção de Erros
Caso você insira algum dado incorreto (como CPF, data ou nome do grupo), a maneira mais fácil de corrigir isso é excluir o arquivo json gerado na primeira execução e rodar o programa novamente. Isso garantirá que você possa redefinir as informações.

7. Frequência de Execução
Recomendamos executar o programa uma vez por semana, preferencialmente às segundas-feiras, para garantir que os alunos recebam as informações atualizadas.

Instruções para instalação
Baixe o executável e coloque-o em uma pasta de sua escolha.

Certifique-se de que o Google Chrome está instalado e configurado corretamente no seu sistema.

Considerações Finais
Este programa foi desenvolvido para ajudar a automatizar o envio de informações sobre workshops aos alunos, economizando tempo e garantindo que todos recebam os lembretes. Para qualquer dúvida ou melhoria, sinta-se à vontade para contribuir com o código no GitHub.
