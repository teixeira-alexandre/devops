# aula 03/07

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import List

app = FastAPI(title="API de Tarefas")


class Tarefa(BaseModel):
    id: int
    titulo: str
    descricao: str
    concluido: bool
    criado_em: datetime


class TarefaResumo(BaseModel):
    id: int
    titulo: str

banco_de_tarefas = []

@app.post("/tarefas", response_model=Tarefa)
def criar_tarefa(tarefa: Tarefa):
    banco_de_tarefas.append(tarefa)
    return tarefa

@app.get("/tarefas", response_model=List[TarefaResumo])
def listar_tarefas():
    return banco_de_tarefas

@app.get("/tarefas/{id}", response_model=Tarefa)
def visualizar_tarefa(id: int):
    for tarefa in banco_de_tarefas:
        if tarefa.id == id:
            return tarefa
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

@app.put("/tarefas/{id}", response_model=Tarefa)
def atualizar_tarefa(id: int, tarefa_atualizada: Tarefa):
    for index, tarefa in enumerate(banco_de_tarefas):
        if tarefa.id == id:
            banco_de_tarefas[index] = tarefa_atualizada
            return tarefa_atualizada
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

@app.delete("/tarefas/{id}")
def excluir_tarefa(id: int):
    for index, tarefa in enumerate(banco_de_tarefas):
        if tarefa.id == id:
            del banco_de_tarefas[index]
            return {"mensagem": "Tarefa excluída com sucesso"}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")


@app.get("/health")
def health_check():
    return {"status": "OK"}

@app.get("/metricas")
def obter_metricas():
    total = len(banco_de_tarefas)
    finalizadas = len([t for t in banco_de_tarefas if t.concluido])
    pendentes = total - finalizadas
    return {
        "quantidade_tarefas": total,
        "tarefas_finalizadas": finalizadas,
        "tarefas_pendentes": pendentes
    }

# aula 04/07

@app.get("/health")
def health_check():
    return {"status": "OK"}


@app.get("/metricas")
def metricas():
    quantidade = len(banco_de_tarefas)
    finalizadas = sum(1 for tarefa in banco_de_tarefas if tarefa.concluido)
    pendentes = quantidade - finalizadas
    
    return {
        "quantidade_tarefas": quantidade,
        "tarefas_finalizadas": finalizadas,
        "tarefas_pendentes": pendentes
    }