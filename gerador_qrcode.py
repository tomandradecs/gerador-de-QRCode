#Este projeto vai te guiar na criacao de um gerador de QR Code simples em Python. Voce usara uma biblioteca esterna para transformar qualquer texto ou URL que o usuario fornecer em uma imagem de QRCode. É uma otima forma de aprender a usar pacotes de terceiros e manipular arquivos de imagem.
#Oque voce vai aprender: instalação de bibliotecas externas, uso de bibliotecas de terceiros, manipulação basica de arquivos, entrada e saida de dados, tratamento de erros.
#Funcionalidades: Entrada de texto ou URL, geracao de QRCode, salvar imagem, mensagem de confirmacao.

import qrcode
def gerar_qrcode(texto, nome_arquivo):
    """
    Gera um QR Code a partir do texto fornecido e salva como imagem.
    
    :param texto: Texto ou URL para gerar o QR Code.
    :param nome_arquivo: Nome do arquivo onde o QR Code será salvo.
    """
    try:
        # Cria o QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(texto)
        qr.make(fit=True)

        # Cria a imagem do QR Code
        img = qr.make_image(fill_color="black", back_color="white")

        # Salva a imagem
        img.save(nome_arquivo)
        print(f"QR Code gerado e salvo como {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao gerar QR Code: {e}")
def main():
    texto = input("Digite o texto ou URL para gerar o QR Code: ")
    nome_arquivo = input("Digite o nome do arquivo para salvar o QR Code (ex: qrcode.png): ")
    
    gerar_qrcode(texto, nome_arquivo)
if __name__ == "__main__":
    main()
# Certifique-se de ter a biblioteca qrcode instalada. Você pode instalar usando o comando:
# pip install qrcode[pil]
# Para executar o script, basta rodar o arquivo Python. Ele solicitará que você insira o texto ou URL e o nome do arquivo para salvar o QR Code.
# O QR Code será gerado e salvo no diretório atual.
# Você pode abrir o arquivo de imagem gerado para verificar o QR Code.
# Dicas adicionais:
# - Experimente gerar QR Codes para diferentes URLs ou textos.
# - Tente alterar as cores do QR Code modificando os parâmetros fill_color e back_color.
# - Explore outras funcionalidades da biblioteca qrcode, como ajustar o tamanho do QR Code ou adicionar imagens ao centro.
# - Considere adicionar tratamento de erros mais robusto, como verificar se o nome do arquivo já existe.
# - Você pode integrar essa funcionalidade em um aplicativo web ou desktop para torná-la mais interativa.
# - Pense em adicionar uma interface gráfica simples usando Tkinter ou PyQt para tornar o gerador de QR Code mais amigável.
# - Considere adicionar a opção de gerar QR Codes para contatos, eventos ou Wi-Fi.
# - Explore a possibilidade de gerar QR Codes dinâmicos que podem ser atualizados sem mudar o código.
# - Pesquise sobre a possibilidade de ler QR Codes usando bibliotecas como OpenCV ou Pyzbar.
# - Pense em criar uma função para ler QR Codes a partir de imagens, complementando o gerador.
# - Considere adicionar a funcionalidade de compartilhar o QR Code gerado diretamente por e-mail ou redes sociais.
# - Explore a possibilidade de gerar QR Codes com diferentes níveis de correção de erros.
# - Pense em criar uma função para gerar QR Codes em lote, permitindo a criação de múltiplos QR Codes de uma vez.
# - Considere adicionar a funcionalidade de personalizar o tamanho do QR Code.
# - Explore a possibilidade de gerar QR Codes animados ou com efeitos visuais.
# - Pense em criar uma função para gerar QR Codes que redirecionem para um site específico.
# - Considere adicionar a funcionalidade de gerar QR Codes que contenham informações de contato (vCard).
# - Explore a possibilidade de gerar QR Codes que abram aplicativos específicos no celular.
# - Pense em criar uma função para gerar QR Codes que contenham informações de localização (geolocalização).
# - Considere adicionar a funcionalidade de gerar QR Codes que contenham informações de eventos (iCal).
# - Explore a possibilidade de gerar QR Codes que contenham informações de Wi-Fi (SSID e senha).
# - Pense em criar uma função para gerar QR Codes que contenham informações de pagamento (como PIX).
# - Considere adicionar a funcionalidade de gerar QR Codes que contenham informações de redes sociais.
# - Explore a possibilidade de gerar QR Codes que contenham informações de produtos (como códigos de barras).
# - Pense em criar uma função para gerar QR Codes que contenham informações de promoções ou cupons.
# - Considere adicionar a funcionalidade de gerar QR Codes que contenham informações de feedback ou pesquisas.
# - Explore a possibilidade de gerar QR Codes que contenham informações de autenticação (como 2FA).
# - Pense em criar uma função para gerar QR Codes que contenham informações de assinatura digital.

