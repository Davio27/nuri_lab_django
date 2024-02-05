# Sistema de Nutrição para Pacientes em Django

Este é um projeto de sistema de nutrição para pacientes desenvolvido em Django. O sistema permite que os nutricionistas registrem informações sobre pacientes, criem planos alimentares personalizados e monitorem o progresso dos pacientes.

## Funcionalidades

- Cadastro de pacientes com informações pessoais e médicas.
- Criação de planos alimentares personalizados para cada paciente.
- Registro do histórico de refeições dos pacientes.
- Acompanhamento do progresso do paciente ao longo do tempo.

## Tecnologias Utilizadas

- Django
- Python
- SQLite (ou outro banco de dados de sua escolha)
- HTML, CSS, JavaScript (para a interface do usuário)

## Configuração do Ambiente Virtual (venv)

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-projeto.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd seu-projeto
   ```

3. Crie um ambiente virtual:

   ```bash
   python -m venv venv
   ```

4. Ative o ambiente virtual:

   - No Windows:

     ```bash
     venv\Scripts\activate
     ```

   - No macOS e Linux:

     ```bash
     source venv/bin/activate
     ```

5. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Configuração do Banco de Dados

1. Execute as migrações:

   ```bash
   python manage.py migrate
   ```

2. Crie um superusuário para acessar a área administrativa:

   ```bash
   python manage.py createsuperuser
   ```

   Siga as instruções para criar um superusuário.

## Como Usar

1. Inicie o servidor:

   ```bash
   python manage.py runserver
   ```

2. Abra o navegador e acesse [http://localhost:8000](http://localhost:8000).

3. Faça login na área administrativa usando as credenciais do superusuário criado.

4. Comece a cadastrar pacientes, criar planos alimentares e registrar o histórico de refeições.

## Estrutura do Projeto

- `nutricao/`: Aplicação principal do Django.
- `pacientes/`: Módulo para gerenciar pacientes.
- `planos_alimentares/`: Módulo para criar planos alimentares.
- `historico_refeicoes/`: Módulo para registrar o histórico de refeições.
- `templates/`: Contém os templates HTML.
- `static/`: Contém arquivos estáticos como CSS, JavaScript, etc.

## Como Contribuir

1. Faça um fork do projeto.
2. Crie uma branch para sua contribuição (`git checkout -b feature/sua-feature`).
3. Faça commit de suas alterações (`git commit -m 'Adiciona nova funcionalidade'`).
4. Faça push para a branch (`git push origin feature/sua-feature`).
5. Abra uma solicitação de pull no GitHub.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.
