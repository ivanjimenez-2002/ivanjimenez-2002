/*NOTE
Use: "npm install @chakra-ui/react@2.8.1 @emotion/react@11.11.1 @emotion/styled@11.11.0 framer-motion@10.12.16 --legacy-peer-deps"
*/
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import { ChakraProvider } from '@chakra-ui/react'
import { BrowserRouter } from 'react-router-dom'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter>
      <ChakraProvider>
        <App />
      </ChakraProvider>
    </BrowserRouter>
  </StrictMode>,
)
