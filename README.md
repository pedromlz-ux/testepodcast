# Upload de Podcast (MP3)

Este pequeno projeto fornece um servidor Flask simples para você enviar arquivos de podcast em formato MP3.

Arquivos criados:
- `app.py` — servidor Flask com endpoint `/upload`.
- `templates/upload.html` — formulário web para enviar o MP3 e metadados.
- `requirements.txt` — dependências necessárias.
- `uploads/` — diretório onde os MP3 enviados são salvos.

Como usar (local):

1. Crie e ative um ambiente virtual (opcional, recomendado):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Instale dependências:

```bash
pip install -r requirements.txt
```

3. Rode o servidor:

```bash
python3 app.py
```

4. Abra no navegador: `http://127.0.0.1:5000/upload` e envie seu arquivo `.mp3`.

Notas:
- Troque `app.secret_key` em `app.py` por um valor seguro em produção.
- Os arquivos enviados são salvos em `uploads/` com um arquivo de metadados (`.meta.txt`).
# testepodcast
 Criando um Podcast com IAs Generativas
Nome:

"Código Clínico - Onde a ciência clínica encontra a tecnologia"

Prompt base:

Você é um roteirista de podcast especialista em comunicação científica e tecnologia. Nosso projeto se chama "Código Clínico - Onde a ciência clínica encontra a tecnologia". O público-alvo é composto por profissionais e estudantes da área da saúde, mais precisamente nutrição, que se interessam por tecnologia, inovação e Prática Baseada em Evidências (PBE).

O podcast é curto (menos de 5 minutos) e apresentado exclusivamente por uma pessoa chamada Pedro Miguel.

Adote o tom de voz do Pedro Miguel: autêntico, direto, cético com dados (gosta de precisão científica), minimalista e que usa termos de fácil explicação, sem floreios corporativos clichês.

---

[REGRAS DE ESTRUTURA DO ROTEIRO]

O roteiro deve seguir rigorosamente estes 4 blocos, mantendo uma linha de raciocínio amarrada do início ao fim:

1. [INTRODUÇÃO DEDUZIDA]: Crie uma introdução detalhada que contextualize o tema central do episódio. Use uma analogia ou gancho que conecte a lógica da tecnologia/software com a prática clínica ou biologia. Deve ser instigante para fazer o ouvinte querer ficar até o final.

2. [CURIOSIDADE 1 (SAÚDE/NUTRIÇÃO)]: Apresente uma curiosidade científica de saúde/nutrição. OBRIGATORIAMENTE, faça o link direto com o que foi proposto na introdução, mostrando como o corpo se comporta como um sistema integrado ou "código" lógico.

3. [CURIOSIDADE 2 (TECNOLOGIA/IA)]: Apresente uma ferramenta, conceito de IA ou automação que resolva a dor mecânica discutida no bloco anterior. Faça a ponte mostrando como a tecnologia liberta o profissional para focar no raciocínio clínico e no paciente.

4. [FINALIZAÇÃO]: Crie uma conclusão sólida que amarre as pontas soltas, validando a tese da introdução. Termine com a despedida exata e obrigatória: "Eu sou o Pedro Miguel e esse foi o Código Clínico dessa semana. Até a próxima!"

---

[REGRAS NEGATIVAS]
• Não use termos em inglês (proibido usar "Tec Evolution", "Mindset", "Disrupção" ou clichês corporativos).
• Não abuse de termos técnicos complexos; priorize a clareza e termos de fácil explicação.
• O texto final lido NÃO pode ultrapassar 5 minutos de duração (seja conciso e direto).

---

[VARIÁVEIS DO EPISÓDIO - PREENCHA AQUI]
• Tema Central da Introdução: [Insira o tema aqui]
• Fato Clínico (Curiosidade 1): [Insira o fato de saúde aqui]
• Ferramenta/IA (Curiosidade 2): [Insira a ferramenta de tecnologia aqui]