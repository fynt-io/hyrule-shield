from hyrule_shield.anonymizer import anonymize_message_spacy

# Lista de mensagens para testar a anonimização
messages = [
    "Meu nome é Carlos Eduardo, meu CPF é 111.222.333-44. Preciso atualizar meu RG, que é 12.345.678-9.",
    "A empresa Tech Solutions Ltda está localizada na Avenida Paulista, 1000, São Paulo, SP.",
    "Entre em contato pelo telefone (11) 98765-4321. Nosso CNPJ é 12.345.678/0001-90.",
    "Olá, sou Ana Carolina e meu CPF é 999.888.777-66. Trabalho na empresa ABC S.A. Nosso escritório fica na Rua das Américas, 123, Rio de Janeiro, RJ. CEP 20000-000.",
    "João da Silva, RG: 23.456.789-0, CPF: 111.222.333-44, mora na Rua do Sol, 456, Bairro do Céu, Cidade Luz, SP, CEP 15000-000.",
    "Olá, aqui é o Fernando. O meu CPF é 123.456.789-00 e o RG é 12.345.678-9.",
    "Gostaria de confirmar se o CNPJ 23.123.456/0001-00 está ativo para realizar uma parceria com a empresa Alpha ME.",
    "Aqui é a Beatriz. Se precisar, meu telefone é (21) 99876-5432.",
    "A sede da Companhia Brasileira está na Alameda dos Anjos, 987, Campinas, SP, CEP 13000-222.",
    "Meu nome é Paulo Henrique. Favor depositar na minha conta bancária usando o CPF 111.222.333-44.",
    "Olá, gostaria de saber qual é o prazo para entrega dos produtos.",
    "Quais são os serviços que vocês oferecem? Estou interessado em algo relacionado a consultoria de TI.",
    "O pedido feito na semana passada ainda não chegou. Gostaria de saber o status.",
    "Bom dia, tudo bem? Estou entrando em contato para saber mais sobre os planos disponíveis.",
    "O produto X tem garantia de 1 ano? Gostaria de mais informações antes de realizar a compra.",
    "Vocês têm uma filial na cidade de Salvador? Preciso visitar uma unidade próxima.",
    "Gostaria de parabenizar toda a equipe pelo excelente atendimento prestado ontem.",
    "Estou enfrentando problemas para acessar a minha conta. Poderiam ajudar?",
    "Quais são os horários de funcionamento da loja física?",
    "Muito obrigado pela rápida resposta e pelo suporte! Fiquei muito satisfeito com o serviço."
]

def main():
    # Iterar sobre cada mensagem e anonimizar
    for i, message in enumerate(messages):
        anonymized_message = anonymize_message_spacy(message)
        print(anonymized_message)
        print("-" * 50)

if __name__ == "__main__":
    main()
