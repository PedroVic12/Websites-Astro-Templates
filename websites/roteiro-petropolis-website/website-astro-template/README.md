# Website Astro Template (MVVM + MUI + Tailwind)

Este é um template moderno para Astro, focado em performance, escalabilidade e design responsivo.

## 🚀 Tecnologias
- **Astro 5.0**: Framework para sites rápidos e focados em conteúdo.
- **Tailwind CSS**: Estilização utilitária mobile-first.
- **Material UI (MUI)**: Componentes de UI profissionais integrados via React.
- **TypeScript**: Segurança de tipos em todo o projeto.

## 🏗️ Arquitetura MVVM
O projeto segue o padrão Model-View-ViewModel para separar a lógica de dados da apresentação:

- **Model (src/content/):** Define as fontes de dados e esquemas usando Astro Content Collections.
- **ViewModel (src/viewmodels/):** Contém a lógica de busca, ordenação e transformação de dados.
- **View (src/pages/ & src/components/):** Componentes Astro e React que consomem o ViewModel para renderizar a interface.

## 📁 Estrutura de Pastas
- `src/components/`: Componentes reutilizáveis (Astro e React).
- `src/content/`: Arquivos Markdown/Content Collections.
- `src/layouts/`: Layouts base do site.
- `src/pages/`: Rotas dinâmicas e estáticas.
- `src/viewmodels/`: Lógica de processamento de dados.

## 🛠️ Como usar
1. Instale as dependências: `npm install`
2. Inicie o servidor de desenvolvimento: `npm run dev`
3. Adicione novos posts em `src/content/blog/`.

## 🎨 Integração MUI
Para usar componentes Material UI, crie componentes React em `src/components/` e utilize a diretiva `client:load` (ou similar) no Astro para habilitar a interatividade.
