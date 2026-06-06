# ✈️ Template ViajaTech (Astro + Tailwind)

Este é um template padronizado para a criação de roteiros de viagem dinâmicos e interativos. Ele foi construído utilizando **Astro** e **Tailwind CSS**, priorizando performance, SEO e facilidade de reutilização via Content Collections.

## 🚀 Como Instalar

### 1. Requisitos Próvios

Certifique-se de que seu projeto tem o Tailwind CSS instalado:

```bash
npx astro add tailwind
```

### 2. Copiando o Template

Basta copiar a pasta `astro-tailwind` para dentro do seu diretório de componentes:
`src/components/templates/astro-tailwind/`

---

## 🛠️ Como Usar no Astro (Nativo)

O template utiliza o componente mestre `TravelPage.astro`. Ele centraliza toda a lógica e layout.

### Exemplo de implementação em uma rota dinâmica

Crie o arquivo `src/pages/viagem/[slug].astro`:

```astro
---
import { getCollection, render } from "astro:content";
import TravelPage from "../../components/templates/astro-tailwind/TravelPage.astro";

export async function getStaticPaths() {
  const posts = await getCollection("viagem");
  return posts.map((post) => ({
    params: { slug: post.id },
    props: { post },
  }));
}

const { post } = Astro.props;
const { Content } = await render(post);
---

<TravelPage data={post.data} Content={Content} />
```

---

## ⚛️ Como Usar no Next.js / React

Para usar no Next.js, você precisará converter os arquivos `.astro` para `.tsx`.

### Passos para Conversão

1. **Props:** No Astro usamos `Astro.props`. No React, passe as props como argumentos da função:
   `export const Hero = ({ images }) => { ... }`
2. **Scripts:** A lógica dentro das tags `<script>` do Astro deve ser movida para hooks `useEffect` ou `useState` no React.
3. **Imagens:** Substitua as tags `<img>` pelo componente `next/image` se estiver usando Next.js para otimização automática.
4. **Classes:** O Tailwind funcionará da mesma forma, basta mudar `class` para `className`.

---

## 🍦 Como Usar em JavaScript Vanilla / HTML

Como este template usa **Tailwind CSS** e **Scripts Inline**, ele é extremamente fácil de portar para HTML puro.

1. **HTML:** Copie a estrutura gerada pelo Astro (inspecionando o elemento no navegador) para seu arquivo `.html`.
2. **CSS:** Adicione o CDN do Tailwind no seu `<head>`:
   `<script src="https://cdn.tailwindcss.com"></script>`
3. **JS:** Copie o conteúdo das tags `<script is:inline>` para um arquivo `.js` separado ou para o final do seu HTML.

---

## 📦 Estrutura de Pastas

- `Layout/`: Componentes globais (Navbar, Toast de notificação).
- `Sections/`: Grandes blocos de conteúdo (Hero, Itinerário, Cards de Informação).
- `UI/`: Componentes atômicos e reutilizáveis (Botões, Modais animados, Checkboxes).

---

## 🎨 Customização de Cores

O template utiliza predominantemente as cores `orange-500` (#ff9800) e `gray-900`.
Para mudar a identidade visual, você pode:

1. Fazer um *find and replace* no VS Code de `orange-500` para a sua cor desejada (ex: `blue-500`).
2. Ou configurar o `tailwind.config.mjs` para mapear essas cores para variáveis de tema.

---

## 📝 Regras do Roteiro (.md)

Para o template funcionar perfeitamente, seu arquivo Markdown deve conter no mínimo:

- `title`: Título da viagem.
- `days`: Lista de objetos com `day`, `title`, `focus` e `events`.
- **Duração mínima recomendada:** 4 dias para preencher bem o layout.

---
*Template mantido por Gemini CLI - 2026*
