#SDK AI GOOGLE GENERATIVE
pip install -q -U google-generativeai

#Adicionar API KEY
import google.generativeai as genai
GOOGLE_API_KEY = 'COLE_SUA_API_AQUI'
genai.configure(api_key=GOOGLE_API_KEY)

#Lista versões de modelo disponíveis
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print (m.name)

#Configurações de temperatura
generation_config = {
    "candidate_count": 1,
    "temperature": 0.8,
}

#Configurações de segurança
safety_settings = {
    "HARASSMENT": "BLOCK_LOW_AND_ABOVE",
    "HATE": "BLOCK_LOW_AND_ABOVE",
    "SEXUAL": "BLOCK_LOW_AND_ABOVE",
    "DANGEROUS": "BLOCK_LOW_AND_ABOVE",
}

#Setup do modelo com configurações criadas
model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config = generation_config,
                              safety_settings = safety_settings)

chat = model.start_chat(history=[])

from IPython.display import Markdown

#Treinando modelo com exemplos de copywrite
treinando_modelo = """
## Tema: E-book para adestrar cães

**Chega de Puxões na Coleira e Latidos Excessivos! Descubra o Guia Completo Para Transformar Seu Cãozinho em um Anjo de Quatro Patas!**

(Imagem/vídeo de um cão feliz e obediente brincando com seu dono em um parque)

Imagine a cena: você passeia tranquilamente com seu cão, sem se preocupar com puxões na coleira ou latidos para outros cachorros. Ele senta, deita e fica ao seu lado, pacientemente esperando por um carinho. Em casa, nada de móveis roídos ou xixi fora do lugar! Parece um sonho? Não precisa ser!

Nós sabemos que você ama seu cão, mas lidar com comportamentos desafiadores pode ser frustrante e estressante. Você já se sentiu desanimado, achando que nunca conseguiria ter o cão dos sonhos?

Apresentamos o Ebook "Adestramento Canino: Guia Completo para um Cão Feliz e Obediente", um método passo-a-passo, testado e aprovado por mais de 10.000 donos de cães, que te guiará na jornada de transformar seu amigo peludo em um companheiro obediente, calmo e feliz!

**O Que Você Encontrará Neste Guia Completo:**

* **Domine os Comandos Básicos:** Ensine seu cão a sentar, deitar, ficar e vir, sem precisar gritar ou repetir mil vezes!
* **Elimine Comportamentos Indesejados:** Diga adeus aos latidos excessivos, xixi no lugar errado, mordidas em tudo e outros hábitos que te tiram do sério!
* **Construa um Vínculo Inabalável:** Fortaleça a relação com seu cão com base em confiança, respeito e comunicação clara.
* **Desfrute de Passeios Relaxantes:** Acabe com os puxões na coleira, os latidos para outros cães e as fugas repentinas. Passeie com tranquilidade e segurança!
* **Decifre a Linguagem Canina:** Aprenda a interpretar cada gesto, cada olhar e cada rosnado do seu cão, comunicando-se com ele de forma eficaz.

Este guia não é apenas um manual de comandos, é um mergulho no mundo canino! Você vai aprender:

* A importância da socialização para um cão equilibrado
* Os erros mais comuns no adestramento e como evitá-los
* Como escolher os melhores brinquedos e acessórios para o seu cão
* Dicas de alimentação para manter seu cão saudável e cheio de energia
* E muito mais!

(Carrossel de imagens com diferentes raças de cães que utilizaram o método com sucesso)

**Veja o que outros donos de cães estão falando sobre o Ebook "Adestramento Canino":**

**(Depoimento 1 com foto do cliente e seu cão)**

"Eu estava prestes a desistir de ter um cachorro! Minha Beagle era um furacão em casa e me arrastava pelas ruas durante os passeios. Graças ao Ebook, hoje ela é um anjo de quatro patas! Recomendo para todos os donos de cães!" - Ana, dona da Luna

**(Depoimento 2 com foto do cliente e seu cão)**

"O Ebook me ensinou a entender meu cão de verdade! Agora, nossa comunicação é muito melhor e ele está muito mais calmo e obediente. As técnicas são simples e fáceis de aplicar. Super recomendo!" - João, dono do Bob

**Aproveite nossa Oferta por Tempo Limitado!**

Adquira agora o Ebook "Adestramento Canino: Guia Completo para um Cão Feliz e Obediente" por apenas R$XX (valor promocional) e receba 3 Bônus Exclusivos:

* **Bônus 1:** Guia Completo de Linguagem Canina: Desvende todos os segredos da comunicação canina!
* **Bônus 2:** 10 Receitas Deliciosas e Saudáveis para o seu cão: Alimente seu melhor amigo com refeições nutritivas e saborosas!
* **Bônus 3:** Grupo VIP no Facebook para tirar dúvidas e compartilhar experiências com outros donos de cães!

E tem mais! Você terá acesso a atualizações vitalícias do Ebook, com novas dicas, técnicas e informações relevantes para o bem-estar do seu cão!

**Sua Satisfação é 100% Garantida!**

Oferecemos uma garantia incondicional de 7 dias. Se, por qualquer motivo, você não estiver satisfeito com o Ebook "Adestramento Canino", basta nos enviar um email e devolveremos seu dinheiro, sem perguntas!

**Clique Aqui e Comece a Transformar a Vida do Seu Cão Hoje Mesmo!**

(Botão de compra com a frase "Quero um Cão Obediente Agora!")

Não perca mais tempo! Diga adeus aos problemas de comportamento e tenha o cão dos sonhos com o nosso Ebook!

(Selos de segurança, garantia e formas de pagamento)

(FAQ com as principais dúvidas sobre o Ebook)

(Informações de contato da empresa)

---

## Tema: Empresa de aluguel de carros

**Esqueça IPVA, Seguro e Manutenção! Viva a Liberdade de Ter um Carro Novo Sem Burocracia com a [Nome da Empresa]!**

(Imagem/vídeo de uma família feliz curtindo um passeio de carro novo em um cenário paradisíaco)

Já imaginou ter um carro zero na garagem, com cheiro de novo e tecnologia de ponta, sem se preocupar com a dor de cabeça de entrada, financiamento ou burocracia? E se, além disso, você pudesse trocar de carro a cada ano, sempre experimentando os últimos lançamentos do mercado?

Com a [Nome da Empresa], isso é possível! Reinvente a forma como você dirige e abrace a liberdade da assinatura de carros. Esqueça os custos ocultos e as preocupações com manutenção, IPVA e seguro. Aqui, você só precisa escolher o carro dos sonhos e aproveitar a viagem!

**O Que a [Nome da Empresa] Oferece?**

* **Frota Diversificada:** Escolha entre uma ampla seleção de carros zero quilômetro, de hatches compactos a SUVs espaçosos, sedans elegantes e até mesmo carros elétricos! Temos o modelo perfeito para o seu estilo de vida.
* **Planos Flexíveis:** Personalize sua assinatura de acordo com suas necessidades. Escolha o período de contrato (12, 24 ou 36 meses) e a quilometragem que melhor se encaixa no seu perfil de uso.
* **Tudo Incluso, Sem Surpresas:** IPVA, seguro, manutenção preventiva e corretiva, assistência 24 horas e carro reserva estão inclusos na sua mensalidade fixa. Desfrute da tranquilidade de ter tudo sob controle, sem custos extras ou imprevistos.
* **Troca Fácil:** Que tal experimentar um modelo diferente a cada ano? Com a [Nome da Empresa], você pode! Troque de carro na renovação do seu contrato e esteja sempre por dentro das últimas tendências do mercado automotivo.
* **Sem Burocracia:** Diga adeus à papelada e às filas intermináveis. Nosso processo de assinatura é 100% online, rápido e descomplicado. Em poucos cliques, você escolhe o carro, personaliza o plano e começa a dirigir!

**A Assinatura de Carros é a Solução Ideal Para:**

* Profissionais que buscam praticidade e economia: Concentre-se no que realmente importa e deixe a gestão do carro com a gente.
* Famílias que precisam de espaço e segurança: Encontre o carro ideal para as necessidades da sua família, com conforto e tranquilidade.
* Amantes de tecnologia e inovação: Esteja sempre por dentro dos últimos lançamentos do mercado automotivo, com a possibilidade de trocar de carro a cada ano.
* Quem valoriza a liberdade e a flexibilidade: Adapte o plano conforme suas necessidades mudam, sem a preocupação de revender o carro ou lidar com contratos longos.

**Comparação entre Ter um Carro Próprio e a Assinatura:**

(Tabela comparativa destacando os custos de IPVA, seguro, manutenção, depreciação e financiamento de um carro próprio versus a mensalidade fixa e a ausência de preocupações da assinatura de carros)

**Experimente a Liberdade de Dirigir Sem Amarras!**

Faça uma simulação online gratuita e descubra o plano de assinatura perfeito para você!

(Botão de chamada para ação: "Simule Agora e Liberte-se!")

**[Nome da Empresa]: Seu Carro Novo, Sem Burocracia, Sem Preocupações!**

(Destaque para os diferenciais da empresa, como: atendimento personalizado, equipe especializada, frota com as melhores marcas e modelos, opções de carros elétricos e híbridos, programa de fidelidade, etc.)

(Informações de contato da empresa: site, telefone, e-mail, redes sociais)

(FAQ com as principais dúvidas sobre a assinatura de carros)

**Liberte-se das amarras do carro próprio e abrace a liberdade sobre quatro rodas!**

(Depoimentos de clientes satisfeitos com a assinatura de carros)

---

## Tema: Curso de WordPress

**Crie Sites Incríveis e Conquiste o Mundo Digital: Torne-se um Mestre do WordPress!**

(Imagem/vídeo de pessoas criando sites bonitos e profissionais em seus laptops, com sorrisos confiantes)

Já imaginou construir sites profissionais e impactantes, sem depender de terceiros e com total liberdade criativa? Sites que geram resultados, conquistam clientes e impulsionam o seu negócio ou projeto? Com o WordPress, tudo isso é possível! E com o nosso curso online completo, você estará pronto para dominar essa plataforma poderosa e abrir as portas para o sucesso no mundo digital.

Deixe de lado o medo do código e as limitações das plataformas prontas!

Nosso curso te guia passo a passo, desde os conceitos básicos até as técnicas mais avançadas, com uma linguagem simples, clara e prática. Você aprenderá:

* **Dominar o WordPress do zero:** Instalação, configuração, painéis de controle, temas, plugins, e tudo o que você precisa saber para se sentir em casa na plataforma.
* **Criar sites incríveis com Elementor:** Explore o poder do construtor de páginas mais popular do mundo, criando layouts profissionais, personalizados e responsivos, sem precisar escrever uma linha de código!
* **Otimizar seu site para SEO:** Alcance as primeiras posições no Google e atraia mais visitantes, aprendendo técnicas eficazes de otimização de conteúdo, palavras-chave e SEO On Page.
* **Gerenciar conteúdo como um profissional:** Crie páginas, posts, categorias, menus, formulários de contato e tudo o que você precisa para um site completo e funcional.
* **Integrar ferramentas poderosas:** Conecte seu site com plataformas de email marketing, redes sociais, sistemas de pagamento e outras ferramentas que potencializam seus resultados.
* **Garantir a segurança do seu site:** Aprenda a proteger seu site contra ataques, hackers e outras ameaças, garantindo a segurança dos seus dados e a confiança dos seus visitantes.

E muito mais! Você terá acesso a um conteúdo completo e sempre atualizado, com:

* **Videoaulas práticas e objetivas:** Aprenda com experts em WordPress, acompanhando exemplos reais e exercícios passo a passo.
* **Material de apoio para download:** Templates, checklists, e-books e outros recursos para você consultar sempre que precisar.
* **Comunidade online exclusiva:** Tire suas dúvidas, troque experiências e conecte-se com outros alunos e instrutores.
* **Certificado de conclusão:** Comprove suas habilidades e destaque-se no mercado de trabalho.

Imagine as possibilidades:

* Criar o site da sua empresa: Promova seus produtos e serviços online, gere leads e aumente suas vendas.
* Desenvolver sites para clientes: Ofereça seus serviços como freelancer ou web designer, construindo uma carreira de sucesso.
* Criar um blog profissional: Compartilhe suas ideias, construa sua marca pessoal e conquiste uma audiência engajada.
* Criar lojas virtuais e vender online: Explore o mundo do e-commerce com o WooCommerce, criando lojas virtuais completas e seguras.

(Carrossel com exemplos de sites incríveis criados com WordPress)

**Investir no seu futuro digital nunca foi tão fácil!**

Matricule-se agora no curso online de WordPress e comece a construir sites incríveis:

(Botão de chamada para ação: "Quero Criar Sites Incríveis!")

**Aproveite nossa oferta por tempo limitado!**

* Acesso vitalício ao curso e suas atualizações
* Bônus exclusivos: curso de SEO, curso de marketing digital, templates premium para Elementor
* Garantia de 7 dias: Se você não ficar satisfeito, devolvemos seu dinheiro!

Não perca tempo! O mundo digital te espera!

(Depoimentos de alunos que transformaram suas vidas com o WordPress)

(Selos de garantia, segurança e formas de pagamento)

(Informações de contato da empresa)
"""

Markdown(treinando_modelo)

#Execução do código para interação com usuário
print('')
chat.send_message(treinando_modelo)
prompt = input('Digite o tema do seu negócio (Ex: Capas de celular personalizadas):')
system_instruction = "Seja muito persuasivo"
response = chat.send_message(system_instruction + ' Crie uma copy completa com o tema ' + prompt)
print(response.text)
print(' \n\n ============================================================= \n\n')
print('Deseja gerar o código da Landing Page?\n\n')
print('Escreva com letras maiusculas\n\n')
gerar_lp = input('SIM | NÃO\n')

if gerar_lp == "SIM":
  response_code = chat.send_message("Transforme essa copy em um site completo, com HTML, CSS e JS")
  print(response_code.text)
else:
  print('Obrigado!\n Recarregue o código se deseja criar um novo conteúdo.')
