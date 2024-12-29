# embbedings
In this repository you will find my first content about embbedings, where I transform a phrase in a embbeding vector using ollama and the free model "mxbai-embed-large". 

Nesse repositório você vai encontrar meus primeiros passos para compreender melhor como funciona as IAs abordando temas como embbedings e tokenização. Para ser mais específico irei demonstrar através de um código python um exemplo de como funciona um embbeding. O programa irá ler uma pequena frase e criar um vetor com 1024 números, esse vetor é responsavel por captar a semantica da frase, ou seja, cada frase criada terá um valor semantico atribuido a ela, dessa forma podemos calcular uma aproximação semantica entre frases usando o calculo da distância de cosseno. Para tornar isso possível utlizei o programa Ollama (https://ollama.com/) e usei o modelo "mxbai-embed-large" disponível em "https://ollama.com/library/mxbai-embed-large".

Instruções para reprodução do ambiente e Orientações para instalação de dependências e execução do script:
1. Baixe e instale o Ollama (https://ollama.com/)
2. Baixe e instale o modelo "mxbai-embed-large" disponível em "https://ollama.com/library/mxbai-embed-large".
     obs: a instalação é feita diretamente através do prompt de comando do Visual Studio Code ou ou ferrramente similar
3. Baixe e instale a biblioteca "numpy" (https://numpy.org/install/) e "langchain_community.embeddings" (pip install -U langchain-ollama)
4. Com o ambiente pronto basta rodar o código e fazer as alterações que desejar
