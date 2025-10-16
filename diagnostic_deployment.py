#!/usr/bin/env python3
"""
Script de diagnóstico para verificar se as mudanças estão sendo aplicadas no Streamlit Cloud.
"""

import sys
import os
import importlib.util

def check_file_exists(file_path):
    """Verifica se um arquivo existe."""
    exists = os.path.exists(file_path)
    print(f"📁 {file_path}: {'✅ EXISTS' if exists else '❌ NOT FOUND'}")
    return exists

def check_function_in_module(module_path, function_name):
    """Verifica se uma função específica existe em um módulo."""
    try:
        spec = importlib.util.spec_from_file_location("test_module", module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        has_function = hasattr(module, function_name)
        print(f"🔍 {function_name} in {module_path}: {'✅ FOUND' if has_function else '❌ NOT FOUND'}")
        return has_function
    except Exception as e:
        print(f"❌ Error checking {module_path}: {e}")
        return False

def check_postprocessor_version():
    """Verifica qual versão do pós-processador está sendo usada."""
    try:
        from src.pdf_postprocessor import PDFPostProcessor
        
        # Verificar se tem os métodos novos
        has_analyze_page_content = hasattr(PDFPostProcessor, '_analyze_page_content')
        has_is_page_truly_empty = hasattr(PDFPostProcessor, '_is_page_truly_empty')
        
        print(f"🧠 PDFPostProcessor._analyze_page_content: {'✅ FOUND' if has_analyze_page_content else '❌ NOT FOUND'}")
        print(f"🧠 PDFPostProcessor._is_page_truly_empty: {'✅ FOUND' if has_is_page_truly_empty else '❌ NOT FOUND'}")
        
        if has_analyze_page_content and has_is_page_truly_empty:
            print("✅ NOVO ALGORITMO INTELIGENTE CARREGADO!")
            return True
        else:
            print("❌ ALGORITMO ANTIGO AINDA ATIVO!")
            return False
            
    except ImportError as e:
        print(f"❌ Erro ao importar PDFPostProcessor: {e}")
        return False

def check_engine_postprocessing():
    """Verifica se o pós-processamento está habilitado no engine."""
    try:
        with open('src/rendering/engine.py', 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'enable_postprocessing = True' in content:
            print("✅ PÓS-PROCESSAMENTO HABILITADO no engine.py")
            return True
        elif 'enable_postprocessing = False' in content:
            print("⚠️ PÓS-PROCESSAMENTO DESABILITADO no engine.py")
            return False
        else:
            print("❓ Status do pós-processamento INDETERMINADO")
            return None
            
    except Exception as e:
        print(f"❌ Erro ao verificar engine.py: {e}")
        return False

def main():
    print("🔍 DIAGNÓSTICO DE DEPLOYMENT - STREAMLIT CLOUD")
    print("=" * 60)
    
    # Verificar arquivos essenciais
    print("\n📁 VERIFICANDO ARQUIVOS:")
    check_file_exists('src/pdf_postprocessor.py')
    check_file_exists('src/core/pdf_finalizer.py')
    check_file_exists('src/rendering/engine.py')
    
    # Verificar funções específicas
    print("\n🔍 VERIFICANDO FUNÇÕES:")
    check_function_in_module('src/pdf_postprocessor.py', '_analyze_page_content')
    check_function_in_module('src/pdf_postprocessor.py', '_is_page_truly_empty')
    
    # Verificar versão do pós-processador
    print("\n🧠 VERIFICANDO ALGORITMO:")
    new_algo = check_postprocessor_version()
    
    # Verificar status do engine
    print("\n⚙️ VERIFICANDO ENGINE:")
    engine_enabled = check_engine_postprocessing()
    
    # Resumo final
    print("\n" + "=" * 60)
    print("📋 RESUMO DO DIAGNÓSTICO:")
    
    if new_algo and engine_enabled:
        print("✅ CONFIGURAÇÃO CORRETA - Novo algoritmo ativo!")
    elif new_algo and not engine_enabled:
        print("⚠️ ALGORITMO OK mas pós-processamento DESABILITADO")
    elif not new_algo:
        print("❌ ALGORITMO ANTIGO ainda ativo - problema de deployment!")
    else:
        print("❓ STATUS INDETERMINADO - investigação manual necessária")
    
    print(f"\n🐍 Python: {sys.version}")
    print(f"📍 Working Directory: {os.getcwd()}")
    print(f"📂 Files in current dir: {len(os.listdir('.'))}")

if __name__ == "__main__":
    main()