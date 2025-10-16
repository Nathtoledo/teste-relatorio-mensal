# main.py
# Roda o Streamlit com verificação de diagnóstico

import sys
import os

# Adicionar diagnóstico de importações
def run_diagnostic():
    """Executa diagnóstico rápido das mudanças."""
    try:
        # Verificar se os arquivos novos existem
        files_to_check = [
            'src/pdf_postprocessor.py',
            'src/core/pdf_finalizer.py'
        ]
        
        missing_files = []
        for file_path in files_to_check:
            if not os.path.exists(file_path):
                missing_files.append(file_path)
        
        if missing_files:
            print(f"❌ ERRO: Arquivos não encontrados: {missing_files}")
            return False
            
        # Verificar se as funções novas existem
        try:
            from src.pdf_postprocessor import PDFPostProcessor
            if not hasattr(PDFPostProcessor, '_analyze_page_content'):
                print("❌ ERRO: Função _analyze_page_content não encontrada - código antigo ativo!")
                return False
            if not hasattr(PDFPostProcessor, '_is_page_truly_empty'):
                print("❌ ERRO: Função _is_page_truly_empty não encontrada - código antigo ativo!")
                return False
            print("✅ Novo algoritmo carregado com sucesso!")
            return True
        except ImportError as e:
            print(f"❌ ERRO DE IMPORTAÇÃO: {e}")
            return False
            
    except Exception as e:
        print(f"❌ ERRO NO DIAGNÓSTICO: {e}")
        return False

# Executar diagnóstico antes de iniciar o Streamlit
print("🔍 Verificando deployment...")
diagnostic_result = run_diagnostic()

if not diagnostic_result:
    print("⚠️ AVISO: Problemas detectados no deployment!")

try:
    from src.interfaces.streamlit_ui import main #prod
    #from src.interfaces.streamlit_ui_dev import main #dev
    
    if __name__ == "__main__":
        main()
except Exception as e:
    print(f"❌ ERRO CRÍTICO ao iniciar Streamlit: {e}")
    print("📋 Informações de debug:")
    print(f"Python: {sys.version}")
    print(f"Working Dir: {os.getcwd()}")
    print(f"Files: {os.listdir('.')[:10]}...")  # Primeiros 10 arquivos
    raise