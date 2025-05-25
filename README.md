README (English)
📝 To-Do List Web Application with User Authentication 🔒


This is a simple yet functional To-Do List web application built using Django. It allows users to manage their tasks efficiently with features including user authentication, task creation ➕, editing ✏️, deletion 🗑️, marking as complete ✅, and filtering 🔍. Users can also set deadlines 📅 for their tasks.

✨ Features
User Authentication: Secure user registration and login system, ensuring each user has their own private task list.


CRUD Operations: Users can Create ➕, Read (list and filter 🔍), Update ✏️ (edit and mark as complete ✅), and Delete 🗑️ their tasks.


Task Creation: Easily add new tasks to your personal to-do list.


Task Editing: Modify the description and deadline ✏️ of existing tasks.


Mark as Complete: Toggle the status of a task to "Completed" ✅.


Task Deletion: Remove tasks that are no longer needed 🗑️.


Deadline Setting: Assign due dates 📅 to tasks to help manage time effectively.


Task Filtering: View tasks based on their status 🔍:


All tasks
Only pending tasks ⏳
Only completed tasks ✅


🛠️ Technologies Used
Django: A high-level Python web framework used for building the application.


HTML: Used for the structure and content of the web pages (template provided).


CSS: Used for the styling and visual presentation of the web pages (stylesheet provided).


Bootstrap: A CSS framework used for providing a responsive and modern user interface.


SQLite: (Default) A lightweight, file-based database used for storing application data (user accounts and tasks).
🚀 Getting Started


To run this project locally, follow these steps:

Clone the repository:

git clone [https://github.com/joaow0/To_do_list]

cd [To_do_list]



Create and activate a virtual environment (recommended):
python -m venv venv
source venv/bin/activate # On macOS/Linux
.\venv\Scripts\activate # On Windows


Install dependencies:
pip install -r requirements.txt
(You might need to create a requirements.txt file if you haven't already. You can do this by running pip freeze > requirements.txt after installing Django and any other necessary packages.)


Make migrations:
python manage.py makemigrations
python manage.py migrate


Create a superuser (for admin access):
python manage.py createsuperuser


Run the development server:
python manage.py runserver


7.  Open your browser and navigate to http://127.0.0.1:8000/tasks/ (or the URL you configured in your urls.py).


🧑‍💻 Usage
Registration/Login: Use the provided registration and login forms to access your personal task list.


Adding Tasks: On the main page, use the "Add New Task" form to create new tasks ➕ and set a deadline 📅.


Viewing Tasks: Your tasks will be listed below, showing their description, deadline 📅, and status.


Filtering Tasks: Use the "Filter Tasks" section to view tasks based on their status 🔍 (All, Pending ⏳, Completed ✅).


Editing Tasks: Each task in the list has an inline form to edit the description ✏️, deadline 📅, and status. Click the "Update" button to save changes.


Marking as Complete: Use the status dropdown to change the status to "Completed" ✅ and click "Update".


Deleting Tasks: Each task has a "Delete" button to remove it from your list 🗑️.


🤝 Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.





README (Português)
📝 Aplicação Web de Lista de Tarefas com Autenticação de Usuário 🔒


Esta é uma aplicação web de Lista de Tarefas simples, porém funcional, construída utilizando Django. Ela permite que usuários gerenciem suas tarefas de forma eficiente com funcionalidades incluindo autenticação de usuário, criação ➕, edição ✏️, exclusão 🗑️, marcação de tarefas como concluídas ✅ e filtragem 🔍. Usuários também podem definir prazos 📅 para as suas tarefas.


✨ Funcionalidades
Autenticação de Usuário: Sistema seguro de registro e login de usuários, garantindo que cada usuário tenha sua própria lista de tarefas privada.


Operações CRUD: Usuários podem Criar ➕, Ler (listar e filtrar 🔍), Atualizar ✏️ (editar e marcar como concluída ✅) e Excluir 🗑️ suas tarefas.


Criação de Tarefas: Adicione facilmente novas tarefas à sua lista pessoal.


Edição de Tarefas: Modifique a descrição e o prazo ✏️ de tarefas existentes.


Marcar como Concluída: Altere o status de uma tarefa para "Concluída" ✅.


Exclusão de Tarefas: Remova tarefas que não são mais necessárias 🗑️.


Definição de Prazo: Atribua datas de vencimento 📅 às tarefas para ajudar no gerenciamento do tempo de forma eficaz.


Filtragem de Tarefas: Visualize tarefas com base em seu status 🔍:


Todas as tarefas
Apenas tarefas pendentes ⏳
Apenas tarefas concluídas ✅


🛠️ Tecnologias Utilizadas
Django: Um framework web Python de alto nível usado para construir a aplicação.


HTML: Usado para a estrutura e o conteúdo das páginas web (template fornecido).


CSS: Usado para o estilo e a apresentação visual das páginas web (stylesheet fornecido).


Bootstrap: Um framework CSS usado para fornecer uma interface de usuário responsiva e moderna.


SQLite: (Padrão) Um banco de dados leve, baseado em arquivo, usado para armazenar os dados da aplicação (contas de usuário e tarefas).


🚀 Primeiros Passos
Para executar este projeto localmente, siga estes passos:


Clone o repositório:
git clone [https://github.com/joaow0/To_do_list)]
cd [To_do_list]


Crie e ative um ambiente virtual (recomendado):
python -m venv venv
source venv/bin/activate # No macOS/Linux
.\venv\Scripts\activate # No Windows


Instale as dependências:
pip install -r requirements.txt
(Você pode precisar criar um arquivo requirements.txt se ainda não o fez. Você pode fazer isso executando pip freeze > requirements.txt após instalar o Django e quaisquer outros pacotes necessários.)


Crie as migrações:
python manage.py makemigrations
python manage.py migrate


Crie um superusuário (para acesso administrativo):
python manage.py createsuperuser


Execute o servidor de desenvolvimento:
python manage.py runserver

Abra seu navegador e navegue para http://127.0.0.1:8000/tasks/ (ou a URL que você configurou em seu urls.py).


🧑‍💻 Utilização
Registro/Login: Use os formulários de registro e login fornecidos para acessar sua lista de tarefas pessoal.


Adicionando Tarefas: Na página principal, use o formulário "Adicionar Nova Tarefa" para criar novas tarefas ➕ e definir um prazo 📅.


Visualizando Tarefas: Suas tarefas serão listadas abaixo, mostrando sua descrição, prazo 📅 e status.


Filtrando Tarefas: Use a seção "Filtrar Tarefas" para visualizar tarefas com base em seu status 🔍 (Todas, Pendentes ⏳, Concluídas ✅).


Editando Tarefas: Cada tarefa na lista possui um formulário inline para editar a descrição ✏️, o prazo 📅 e o status. Clique no botão "Atualizar" para salvar as alterações.


Marcar como Concluída: Use o menu dropdown de status para alterar o status para "Concluída" ✅ e clique em "Atualizar".


Excluindo Tarefas: Cada tarefa possui um botão "Deletar" para removê-la da sua lista 🗑️.


🤝 Contribuições
Contribuições são bem-vindas! Se você gostaria de contribuir para este projeto, por favor, faça um fork do repositório e envie um pull request com suas alterações.

