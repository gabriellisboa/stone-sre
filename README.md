
# Random number service

Feito pro teste de SRE da Stone.

Este projeto usa o [Flask](https://flask.palletsprojects.com/en/2.2.x/) pra criar um serviço que retorna um número aleatório.

As métricas são expostas com o [Prometheus-flask-exporter](https://pypi.org/project/prometheus-flask-exporter/) e capituradas pelo [FluentBit](https://fluentbit.io/)

Os logs são escritos em um arquivo e também capiturados pelo [FluentBit](https://fluentbit.io/)


O Fluentbit está com o *output* configurado pro *stdout* então você pode ver as métricas e logs no output do console.
Isso pode ser fácilmente redirecionado pra alguma ferramenta de exibição e alerta:
[FluentBit Outputs](https://docs.fluentbit.io/manual/pipeline/outputs)

## Rodando 🎰

```
docker compose up
```


## Documentação da API

#### Retorna número aleatório

```http
  GET /
```

#### Retorna as métricas

```http
  GET /metrics
```



