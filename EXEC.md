# Comandos de execução do código

## Para rodar o STREAMLIT

`.\.venv\Scripts\Activate.ps1 & python -m streamlit run main.py`

Acessar <http://localhost:8501/embed=true?is_admin=true> para visualizar o 'front' do Streamlit que será mostrado na Plataforma IZE.

## Para rodar a API (Swagger)

`.venv\Scripts\python.exe app.py`

## Para testar o pós-processamento de PDFs

`.venv\Scripts\python.exe test_postprocessor.py`

Este comando testa o algoritmo inteligente de detecção de páginas vazias.

<!-- Force redeploy: 2025-10-16 -->
