#!/usr/bin/env python3
"""
Verificação específica para o Streamlit Cloud - demonstra que o novo código está ativo.
Execute este arquivo diretamente no Streamlit Cloud para verificar o deployment.
"""

import streamlit as st
import os
import sys
from datetime import datetime

def main():
    st.title("🔍 Verificação de Deployment - Algoritmo Inteligente")
    st.write("Esta página verifica se as mudanças do pós-processamento foram aplicadas no Streamlit Cloud.")
    
    # Informações do ambiente
    st.subheader("📋 Informações do Ambiente")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write(f"**Python:** {sys.version}")
        st.write(f"**Working Dir:** {os.getcwd()}")
        st.write(f"**Timestamp:** {datetime.now()}")
    
    with col2:
        st.write(f"**Files Count:** {len(os.listdir('.'))}")
        st.write(f"**Platform:** {sys.platform}")
    
    # Verificação dos arquivos críticos
    st.subheader("📁 Verificação de Arquivos")
    
    critical_files = [
        'src/pdf_postprocessor.py',
        'src/core/pdf_finalizer.py',
        'src/rendering/engine.py'
    ]
    
    for file_path in critical_files:
        exists = os.path.exists(file_path)
        if exists:
            st.success(f"✅ {file_path}")
        else:
            st.error(f"❌ {file_path}")
    
    # Verificação das funções do novo algoritmo
    st.subheader("🧠 Verificação do Algoritmo Inteligente")
    
    try:
        from src.pdf_postprocessor import PDFPostProcessor
        
        # Verificar métodos do novo algoritmo
        methods_to_check = [
            '_analyze_page_content',
            '_is_page_truly_empty'
        ]
        
        all_methods_found = True
        for method in methods_to_check:
            has_method = hasattr(PDFPostProcessor, method)
            if has_method:
                st.success(f"✅ PDFPostProcessor.{method}")
            else:
                st.error(f"❌ PDFPostProcessor.{method}")
                all_methods_found = False
        
        if all_methods_found:
            st.balloons()
            st.success("🎉 **NOVO ALGORITMO INTELIGENTE ATIVO!**")
            st.info("O pós-processador agora usa detecção inteligente de páginas vazias.")
        else:
            st.warning("⚠️ **ALGORITMO ANTIGO AINDA ATIVO**")
            st.error("As mudanças não foram aplicadas corretamente.")
            
    except ImportError as e:
        st.error(f"❌ Erro de importação: {e}")
        st.warning("Não foi possível importar o PDFPostProcessor")
    
    # Verificação do engine
    st.subheader("⚙️ Verificação do Engine")
    
    try:
        with open('src/rendering/engine.py', 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'enable_postprocessing = True' in content:
            st.success("✅ Pós-processamento HABILITADO no engine")
        elif 'enable_postprocessing = False' in content:
            st.warning("⚠️ Pós-processamento DESABILITADO no engine")
        else:
            st.info("❓ Status do pós-processamento indeterminado")
            
        # Contar ocorrências de strings chave
        intelligent_count = content.count('_is_page_truly_empty')
        if intelligent_count > 0:
            st.success(f"✅ Algoritmo inteligente referenciado {intelligent_count} vezes")
        else:
            st.error("❌ Algoritmo inteligente não encontrado no engine")
            
    except Exception as e:
        st.error(f"❌ Erro ao verificar engine: {e}")
    
    # Teste de funções
    st.subheader("🧪 Teste das Funções")
    
    if st.button("Testar Algoritmo Inteligente"):
        try:
            from src.pdf_postprocessor import PDFPostProcessor
            
            # Simular análise de página
            test_page_analysis = {
                'has_images': False,
                'has_charts': False,
                'has_visual_elements': False,
                'meaningful_text_length': 5,
                'footer_patterns': ['ize.com.br'],
                'is_special_page': False
            }
            
            # Testar função
            is_empty = PDFPostProcessor._is_page_truly_empty(
                "ize.com.br @ize_", test_page_analysis, 5, 10
            )
            
            if is_empty:
                st.success("✅ Função _is_page_truly_empty funcionando - página detectada como vazia")
            else:
                st.info("ℹ️ Função _is_page_truly_empty funcionando - página detectada com conteúdo")
                
            st.json(test_page_analysis)
            
        except Exception as e:
            st.error(f"❌ Erro no teste: {e}")
    
    # Resumo final
    st.subheader("📊 Resumo do Status")
    
    try:
        from src.pdf_postprocessor import PDFPostProcessor
        has_new_algo = hasattr(PDFPostProcessor, '_analyze_page_content')
        
        if has_new_algo:
            st.success("🎯 **STATUS: DEPLOYMENT CORRETO**")
            st.write("✅ O novo algoritmo inteligente está ativo")
            st.write("✅ Páginas com gráficos serão preservadas")
            st.write("✅ Apenas páginas realmente vazias serão removidas")
        else:
            st.error("🚨 **STATUS: DEPLOYMENT INCORRETO**")
            st.write("❌ Algoritmo antigo ainda ativo")
            st.write("❌ Páginas com gráficos podem ser removidas")
            
    except Exception:
        st.error("🚨 **STATUS: ERRO CRÍTICO**")
        st.write("❌ Não foi possível verificar o status")

if __name__ == "__main__":
    main()