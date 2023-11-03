# Fine Tuning
### Pro del Fine-Tuning di Modelli LLM:

- Adattabilità a compiti specifici: Il fine-tuning consente di adattare un modello LLM a un compito particolare, rendendolo altamente specializzato per quell'applicazione. Questo lo rende molto flessibile e adatto a una vasta gamma di compiti di elaborazione del linguaggio naturale.
- Miglioramento delle prestazioni: I modelli LLM di base, come GPT-3 o BERT, hanno una comprensione generale del linguaggio, ma possono non essere ottimali per compiti specifici. Il fine-tuning permette di migliorare notevolmente le prestazioni su quei compiti, spesso superando altri modelli specializzati.
- Risparmio di tempo e risorse: Addestrare un modello LLM da zero richiede enormi risorse in termini di tempo e potenza di calcolo. Il fine-tuning è solitamente più rapido ed efficiente, poiché si basa su un modello di base pre-allenato.
- Necessità di meno dati etichettati: Mentre l'addestramento da zero richiede grandi quantità di dati etichettati, il fine-tuning può essere realizzato con dataset più piccoli, il che è utile quando i dati etichettati sono limitati.

### Contro del Fine-Tuning di Modelli LLM:

- Dipendenza dai dati di fine-tuning: La qualità del modello fine-tuned dipende dalla qualità dei dati etichettati utilizzati nel processo di fine-tuning. Se i dati etichettati non sono rappresentativi o contengono bias, il modello eredita tali problematiche.
- Overfitting: Il fine-tuning eccessivo su un dataset specifico può portare al fenomeno dell'overfitting, in cui il modello si adatta troppo ai dati di addestramento e non generalizza bene su nuovi dati.
- Risorse computazionali: Anche se il fine-tuning è più efficiente rispetto all'addestramento da zero, richiede ancora risorse computazionali significative per eseguire il processo, in particolare per modelli LLM di grandi dimensioni.
- Manutenzione e aggiornamenti: I modelli fine-tuned possono richiedere manutenzione costante per rimanere allineati con le esigenze in evoluzione del compito. Gli aggiornamenti richiedono di ricominciare il processo di fine-tuning.
- Complessità nella selezione dei modelli base: La scelta di quale modello base utilizzare come punto di partenza per il fine-tuning può essere una decisione critica e richiede una buona comprensione delle esigenze specifiche del compito.

# Prompt Engineering
### Pro del Prompt Engineering con Modelli LLM:

- Flessibilità: Il prompt engineering offre un alto grado di flessibilità nell'adattare un modello LLM a una vasta gamma di compiti. È possibile definire prompt specifici per il compito desiderato, consentendo un controllo preciso sulla generazione di testo.
- Velocità di implementazione: L'implementazione del prompt engineering è spesso più rapida rispetto al fine-tuning di un modello LLM. Non è necessario addestrare il modello da zero o raccogliere grandi quantità di dati etichettati.
- Aumento delle prestazioni: Un prompt ben progettato può migliorare le prestazioni del modello LLM su compiti specifici. Questo può tradursi in una maggiore accuratezza e coerenza nella generazione di testo.
- Risorse ridotte: Rispetto al fine-tuning, il prompt engineering richiede meno risorse computazionali ed è più leggero in termini di memoria e potenza di calcolo.

### Contro del Prompt Engineering con Modelli LLM:

- Complessità nella progettazione dei prompt: La creazione di prompt efficaci richiede un'analisi attenta del compito e delle esigenze specifiche. Un prompt inappropriato può portare a risultati insoddisfacenti.
- Limitazioni semantiche: I modelli LLM con prompt engineering possono essere limitati dalla capacità semantica dei prompt stessi. Se un compito richiede comprensione oltre la sintassi del prompt, il modello potrebbe fallire.
- Sensibilità ai cambiamenti nei dati di input: I modelli con prompt engineering possono essere sensibili a piccole variazioni nei dati di input. 
- Complessità nell'ottimizzazione: La messa a punto dei prompt può essere un processo iterativo, e trovare il prompt ottimale può richiedere tempo e sforzi considerevoli.
- Possibilità di generazione incoerente: In alcuni casi, i modelli con prompt engineering possono generare output incoerente o non pertinenti se i prompt sono formulati in modo ambiguo o non specifico.

# Generative Models
### Pro dei Modelli LLM Generativi:

- Generazione di Testo Creativo: Questi modelli eccellono nella generazione di testo creativo, inclusi scritti, poesie, narrativa e molto altro. Sono spesso utilizzati in applicazioni che richiedono la creazione di contenuti originali.
- Completamento Automatico di Frasi: Possono essere utilizzati per completare frasi o testi in modo coerente. Questa funzionalità è utile in applicazioni come la correzione automatica, la predizione del testo e la scrittura assistita.
- Applicazioni di Dialogo: I modelli generativi sono spesso impiegati in chatbot e sistemi di dialogo, poiché possono generare risposte a input degli utenti in modo naturale e coerente.
- Scalabilità: I modelli generativi possono essere dimensionati per adattarsi a una vasta gamma di compiti e dati. Sono in grado di affrontare compiti di dimensioni variabili.

### Contro dei Modelli LLM Generativi:
- Rischio di Generazione di Contenuti Inappropriati o Bias: I modelli generativi possono generare contenuti inappropriati o contenenti bias. Questo rappresenta una preoccupazione etica e richiede misure di moderazione e controllo.
- Mancanza di Controllo: In alcuni casi, questi modelli possono generare testo incoerente o non rilevante, e non c'è sempre un controllo preciso sulla generazione.
- Overfitting: I modelli generativi possono soffrire di overfitting, in particolare se sono addestrati su dati di dimensioni limitate o se il processo di addestramento non è adeguatamente regolato.
- Richiesta di Risorse Computazionali: I modelli generativi di alta qualità richiedono risorse computazionali considerevoli per l'addestramento e l'inferenza. Possono non essere pratici su dispositivi con risorse limitate.
- Variabilità della Qualità del Testo Generato: La qualità del testo generato può variare notevolmente in base alle condizioni e alle modalità di generazione, e potrebbe richiedere un'ottimizzazione significativa per raggiungere risultati desiderati.

# Differenze tra approcci
Le principali differenze tra questi approcci riguardano l'obiettivo principale e il metodo di guida del modello:
- Gli **approcci generativi** sono progettati per generare testo in modo autonomo, senza necessità di istruzioni specifiche. Questi modelli creano testo basandosi su dati di addestramento e sulla conoscenza appresa durante il pre-training.
- Nel **prompt engineering**, si utilizzano istruzioni o prompt specifici per guidare il modello nella generazione di testo. Questi prompt forniscono una struttura o un contesto per il compito da eseguire. L'obiettivo è di ottenere risposte coerenti e specifiche.
- Il **fine-tuning** implica invece l'adattamento di un modello pre-allenato a compiti specifici utilizzando dati etichettati. Questo processo migliora le prestazioni del modello su un compito specifico, rendendolo più accurato.
  
# Large Language Model

- Llama (Licenza non commerciale/ricerca)
- Llama 2 ([Licenza Llama2 ](https://ai.meta.com/llama/license/) non open-source)
- Falcon ([Apache 2.0](https://www.linux.it/opensource/licenze/licenses/apache-2.0/))
- GPT-3 (Ottenibile solo tramite interfaccia)
- GPT-Neo ([Licenza MIT](https://www.linux.it/opensource/licenze/licenses/mit/), prestazione leggermente inferiori GPT-3)
- GPT-J ([Apache 2.0](https://www.linux.it/opensource/licenze/licenses/apache-2.0/), stile simile GPT-3)
- GTP-4 (Pagamento Plus 20€/mo)