#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Criando bot telegram
import telebot
import cx_Oracle as ocl
import pandas as pd
import dataframe_image as di
import warnings
import time

from datetime import datetime

#ocl.init_oracle_client(lib_dir=r"C:\oracle\instantclient_11_2")

with warnings.catch_warnings():
    warnings.simplefilter('ignore', UserWarning)

    con = ocl.connect('perf/per2013_@192.168.7.33/COMETA')
    query = con.cursor()

    CHAVE_API = "5287629155:AAFJBQ3F9uwcFT1u6NqWkScb3qtRlYZYE9I"

    #Criando o Bot
    bot = telebot.TeleBot(CHAVE_API)

    def verificar(mensagem):
        return True

    #Decorator para condicionar a resposta ao bot
    @bot.message_handler(func=verificar)
    def responder(mensagem):
        if (mensagem.text == "V") or (mensagem.text == "v"): 

            resultado_consulta1 = pd.read_sql_query("""select E.NOMEREDUZIDO,
                sum( ( round( V.VLRITEM, 2 ) ) - ( round( V.VLRDEVOLITEM, 2 ) - ( 0 ) ) )
                as VLRVENDA,
                ROUND((round( sum(
                 CONSINCO.fC5_AbcDistribLucratividade(
                 'L',
                 'L',
                 'N',
                 round( V.VLRITEM, 2 ) ,
                 'N',
                 V.VLRICMSST,
                 V.VLRFCPST,
                 V.VLRICMSSTEMPORIG,
                 E.UF,
                 V.UFPESSOA,
                 'N',
                 0, 
                 'N',
                 V.VLRIPIITEM,
                 V.VLRIPIDEVOLITEM,
                 'N',
                 V.VLRDESCFORANF,
                 Y.CMDIAVLRNF - 0 ,
                 Y.CMDIAIPI,
                 nvl( Y.CMDIACREDPIS, 0 ),
                 nvl( Y.CMDIACREDCOFINS, 0 ),
                 Y.CMDIAICMSST,
                 Y.CMDIADESPNF,
                 Y.CMDIADESPFORANF,
                 Y.CMDIADCTOFORANF,
                 'S',
                 a.propqtdprodutobase,
                 V.QTDITEM,
                 V.VLREMBDESCRESSARCST,
                 V.ACMCOMPRAVENDA,
                 V.PISITEM,
                 V.COFINSITEM,
                 Y.QTDVDA,
                 ( Y.VLRIMPOSTOVDA - nvl( Y.VLRIPIVDA, 0 ) ),
                 'N',
                 V.VLRDESPOPERACIONALITEM,
                 Y.VLRDESPESAVDA,
                 'N',
                 nvl( Y.VLRVERBAVDAACR, 0 ),

                 Y.QTDVERBAVDA,
                 Y.VLRVERBAVDA - nvl( Y.VLRVERBAVDAINDEVIDA, 0 ),

                 'N',
                 V.VLRTOTCOMISSAOITEM,
                 V.VLRDEVOLITEM,
                 VLRDEVOLICMSST,
                 V.DVLRFCPST,
                 V.QTDDEVOLITEM,
                 V.PISDEVOLITEM,
                 V.COFINSDEVOLITEM,
                 V.VLRDESPOPERACIONALITEMDEVOL,
                 V.VLRTOTCOMISSAOITEMDEVOL,
                 E.PERIRLUCRAT,
                 E.PERCSLLLUCRAT,
                 Y.CMDIACREDICMS,
                 decode( V.ICMSEFETIVOITEM, 0, V.ICMSITEM, V.ICMSEFETIVOITEM ),
                 V.VLRFCPICMS,
                 V.PERCPMF,
                 V.PEROUTROIMPOSTO,
                 decode( V.ICMSEFETIVODEVOLITEM, 0, V.ICMSDEVOLITEM, V.ICMSEFETIVODEVOLITEM ),
                 V.DVLRFCPICMS, 
                 case when ( 'S' ) = 'N' then
                 (nvl(y.cmdiavlrdescpistransf,0) + nvl(y.cmdiavlrdesccofinstransf,0) + nvl(y.cmdiavlrdescicmstransf,0) +
                 nvl(y.cmdiavlrdescipitransf,0) + nvl(y.cmdiavlrdesclucrotransf,0) + nvl(y.cmdiavlrdescverbatransf,0) )

                 else 0
                 end, 
                 case when DV.UTILACRESCCUSTPRODRELAC = 'S' and nvl( A.SEQPRODUTOBASE, A.SEQPRODUTOBASEANTIGO ) is not null then
                 coalesce( PR.PERCACRESCCUSTORELACVIG, nvl( CONSINCO.F_RETACRESCCUSTORELACABC( V.SEQPRODUTO, V.DTAVDA ), 1 ) )
                 else 1 
                 end,
                 'N',
                 0,
                 0,
                 'S',
                 V.VLRDESCMEDALHA,
                 'S',
                 V.VLRDESCFORNEC,
                 V.VLRDESCFORNECDEVOL,
                 'N',
                 V.VLRFRETEITEMRATEIO,
                 V.VLRFRETEITEMRATEIODEV,
                 'S',
                 V.VLRICMSSTEMBUTPROD,
                 V.VLRICMSSTEMBUTPRODDEV,
                 V.VLREMBDESCRESSARCSTDEVOL, 
                 v.vlrdescacordoverbapdv,
                 nvl( Y.CMDIACREDIPI, 0 ),
                 NVL(V.VLRITEMRATEIOCTE,0),
                 'N'
                 )
                ), 2 ))*100/sum( ( round( V.VLRITEM, 2 ) ) - ( round( V.VLRDEVOLITEM, 2 ) - ( 0 ) ) ),2)

                as MARGEMLUCRAT

                from CONSINCO.MRL_CUSTODIA Y, CONSINCO.MAXV_ABCDISTRIBBASE V, CONSINCO.MAP_PRODUTO A, CONSINCO.MAP_PRODUTO PB, CONSINCO.MAP_FAMDIVISAO D, CONSINCO.MAP_FAMEMBALAGEM K, CONSINCO.MAX_EMPRESA E, CONSINCO.MAX_DIVISAO DV, CONSINCO.MAP_PRODACRESCCUSTORELAC PR where D.SEQFAMILIA = A.SEQFAMILIA
                and D.NRODIVISAO = V.NRODIVISAO
                and V.SEQPRODUTO = A.SEQPRODUTO
                and V.SEQPRODUTOCUSTO = PB.SEQPRODUTO
                and V.NROEMPRESA in ( 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,27,28,29,30,31,32,34,35,36,37,38,39,40)
                and V.NROSEGMENTO in ( 3,1,2 )
                and V.NRODIVISAO = D.NRODIVISAO
                and E.NROEMPRESA = V.NROEMPRESA
                and E.NRODIVISAO = DV.NRODIVISAO
                AND V.SEQPRODUTO = PR.SEQPRODUTO(+)
                AND V.DTAVDA = PR.DTAMOVIMENTACAO(+)
                and V.DTAVDA = TRUNC(SYSDATE)
                --And V.DTAVDA between TRUNC(DTAVDA_INICIAL) and TRUNC(DTAVDA_FINAL)
                and Y.NROEMPRESA = nvl( E.NROEMPCUSTOABC, E.NROEMPRESA ) 
                and Y.DTAENTRADASAIDA = V.DTAVDA
                 and K.SEQFAMILIA = A.SEQFAMILIA and K.QTDEMBALAGEM = 1 
                and Y.SEQPRODUTO = PB.SEQPRODUTO
                and V.CODGERALOPER in ( 307,308 )
                group by E.NROEMPRESA,
                V.dtavda,
                to_number( null ),
                E.Nomereduzido,
                to_number( null ),
                to_number( null ),
                null

                order by VLRVENDA DESC""", con)
            resultado_consulta2 =  pd.read_sql_query("""select
                'TOTAL' as NOMEREDUZIDO,
               TO_CHAR(sum( ( round( V.VLRITEM, 2 ) ) - ( round( V.VLRDEVOLITEM, 2 ) - ( 0 ) ) ),'FM999G999G999D90', 'nls_numeric_characters='',.''')
                as VLRVENDA,
                ROUND((round( sum(
                 CONSINCO.fC5_AbcDistribLucratividade(
                 'L',
                 'L',
                 'N',
                 round( V.VLRITEM, 2 ) ,
                 'N',
                 V.VLRICMSST,
                 V.VLRFCPST,
                 V.VLRICMSSTEMPORIG,
                 E.UF,
                 V.UFPESSOA,
                 'N',
                 0, 
                 'N',
                 V.VLRIPIITEM,
                 V.VLRIPIDEVOLITEM,
                 'N',
                 V.VLRDESCFORANF,
                 Y.CMDIAVLRNF - 0 ,
                 Y.CMDIAIPI,
                 nvl( Y.CMDIACREDPIS, 0 ),
                 nvl( Y.CMDIACREDCOFINS, 0 ),
                 Y.CMDIAICMSST,
                 Y.CMDIADESPNF,
                 Y.CMDIADESPFORANF,
                 Y.CMDIADCTOFORANF,
                 'S',
                 a.propqtdprodutobase,
                 V.QTDITEM,
                 V.VLREMBDESCRESSARCST,
                 V.ACMCOMPRAVENDA,
                 V.PISITEM,
                 V.COFINSITEM,
                 Y.QTDVDA,
                 ( Y.VLRIMPOSTOVDA - nvl( Y.VLRIPIVDA, 0 ) ),
                 'N',
                 V.VLRDESPOPERACIONALITEM,
                 Y.VLRDESPESAVDA,
                 'N',
                 nvl( Y.VLRVERBAVDAACR, 0 ),

                 Y.QTDVERBAVDA,
                 Y.VLRVERBAVDA - nvl( Y.VLRVERBAVDAINDEVIDA, 0 ),

                 'N',
                 V.VLRTOTCOMISSAOITEM,
                 V.VLRDEVOLITEM,
                 VLRDEVOLICMSST,
                 V.DVLRFCPST,
                 V.QTDDEVOLITEM,
                 V.PISDEVOLITEM,
                 V.COFINSDEVOLITEM,
                 V.VLRDESPOPERACIONALITEMDEVOL,
                 V.VLRTOTCOMISSAOITEMDEVOL,
                 E.PERIRLUCRAT,
                 E.PERCSLLLUCRAT,
                 Y.CMDIACREDICMS,
                 decode( V.ICMSEFETIVOITEM, 0, V.ICMSITEM, V.ICMSEFETIVOITEM ),
                 V.VLRFCPICMS,
                 V.PERCPMF,
                 V.PEROUTROIMPOSTO,
                 decode( V.ICMSEFETIVODEVOLITEM, 0, V.ICMSDEVOLITEM, V.ICMSEFETIVODEVOLITEM ),
                 V.DVLRFCPICMS, 
                 case when ( 'S' ) = 'N' then
                 (nvl(y.cmdiavlrdescpistransf,0) + nvl(y.cmdiavlrdesccofinstransf,0) + nvl(y.cmdiavlrdescicmstransf,0) +
                 nvl(y.cmdiavlrdescipitransf,0) + nvl(y.cmdiavlrdesclucrotransf,0) + nvl(y.cmdiavlrdescverbatransf,0) )

                 else 0
                 end, 
                 case when DV.UTILACRESCCUSTPRODRELAC = 'S' and nvl( A.SEQPRODUTOBASE, A.SEQPRODUTOBASEANTIGO ) is not null then
                 coalesce( PR.PERCACRESCCUSTORELACVIG, nvl( CONSINCO.F_RETACRESCCUSTORELACABC( V.SEQPRODUTO, V.DTAVDA ), 1 ) )
                 else 1 
                 end,
                 'N',
                 0,
                 0,
                 'S',
                 V.VLRDESCMEDALHA,
                 'S',
                 V.VLRDESCFORNEC,
                 V.VLRDESCFORNECDEVOL,
                 'N',
                 V.VLRFRETEITEMRATEIO,
                 V.VLRFRETEITEMRATEIODEV,
                 'S',
                 V.VLRICMSSTEMBUTPROD,
                 V.VLRICMSSTEMBUTPRODDEV,
                 V.VLREMBDESCRESSARCSTDEVOL, 
                 v.vlrdescacordoverbapdv,
                 nvl( Y.CMDIACREDIPI, 0 ),
                 NVL(V.VLRITEMRATEIOCTE,0),
                 'N'
                 )
                ), 2 ))*100/sum( ( round( V.VLRITEM, 2 ) ) - ( round( V.VLRDEVOLITEM, 2 ) - ( 0 ) ) ),2)
                as MARGEMLUCRAT
                from CONSINCO.MRL_CUSTODIA Y, CONSINCO.MAXV_ABCDISTRIBBASE V, CONSINCO.MAP_PRODUTO A, CONSINCO.MAP_PRODUTO PB, CONSINCO.MAP_FAMDIVISAO D, CONSINCO.MAP_FAMEMBALAGEM K, CONSINCO.MAX_EMPRESA E, CONSINCO.MAX_DIVISAO DV, CONSINCO.MAP_PRODACRESCCUSTORELAC PR where D.SEQFAMILIA = A.SEQFAMILIA
                and D.NRODIVISAO = V.NRODIVISAO
                and V.SEQPRODUTO = A.SEQPRODUTO
                and V.SEQPRODUTOCUSTO = PB.SEQPRODUTO
                and V.NROEMPRESA in ( 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,27,28,29,30,31,32,34,35,36,37,38,39,40)
                and V.NROSEGMENTO in ( 3,1,2 )
                and V.NRODIVISAO = D.NRODIVISAO
                and E.NROEMPRESA = V.NROEMPRESA
                and E.NRODIVISAO = DV.NRODIVISAO
                AND V.SEQPRODUTO = PR.SEQPRODUTO(+)
                AND V.DTAVDA = PR.DTAMOVIMENTACAO(+)
                and V.DTAVDA = TRUNC(SYSDATE)
                and Y.NROEMPRESA = nvl( E.NROEMPCUSTOABC, E.NROEMPRESA ) 
                and Y.DTAENTRADASAIDA = V.DTAVDA
                 and K.SEQFAMILIA = A.SEQFAMILIA and K.QTDEMBALAGEM = 1 
                and Y.SEQPRODUTO = PB.SEQPRODUTO



                and V.CODGERALOPER in ( 307,308 )""", con)
            
            #time.sleep(2)
            warnings.simplefilter(action='ignore', category=FutureWarning) 
            #venda = resultado_consulta.fillna('Total até as ')
            venda = pd.concat([resultado_consulta1,resultado_consulta2], ignore_index= True)
            #venda = venda.set_index(['Loja', 'Venda', 'Margem'])
            di.export(venda, r"venda.png")
            
            
            venda = open(r"venda.png", "rb")
            bot.send_photo(mensagem.chat.id, venda)
            venda.close()
        elif mensagem.text == "euro":
            bot.send_message(mensagem.chat.id, 'Euro: {}'.format(cotacoes_dic["EUR"]["bid"]))
        else:
            bot.send_message(mensagem.chat.id, 'Comando não reconhecido!')

bot.polling()


# In[ ]:




