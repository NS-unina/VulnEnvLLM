# Linee guida uso GitHub
Di seguito una lista di convenzioni per la realizzazione del progetto su GitHub


## Linee guida per scrivere buon codice 
- Il codice sorgente deve essere salvato all'interno di un repository git. 

-  Il codice sorgente deve contenere un README.md utilizzando il seguente modello: https://gist.github.com/PurpleBooth/109311bb0361f32d87a2.
- Tutte le informazioni rilevanti devono essere inserite nel README.md. Non ci devono essere file nascosti nelle sotto-cartelle che spieghino come usarlo.
- Il codice sorgente deve essere caricato nel repository git all'inizio della tesi, non alla fine.
- Se stai utilizzando un ambiente di sviluppo integrato (IDE), per favore, non salvare i file di configurazione dell'IDE nel repository git. Per favore, utilizza il file .gitignore disponibile qui: https://github.com/github/gitignore.
- Se il codice sorgente ha delle dipendenze da moduli, deve essere creato un file di requisiti, ad esempio:

- Per Node.js, utilizza package.json. Quando installi un modulo, salvane i dettagli con "npm install --save <package>".
-jPer Java, utilizza Gradle o Maven.
- Il codice sorgente deve essere testato su una macchina di test e non deve essere utilizzato a scopo di sviluppo. Non deve essere testato solo sulla macchina utilizzata durante lo sviluppo, poiché potrebbe darsi che durante la fase di sviluppo tu abbia creato condizioni che rendono impossibile l'utilizzo del tuo codice in un altro ambiente. Per favore, testa il tuo codice in un ambiente diverso.
- Tutti i parametri configurabili devono essere collocati in una directory di configurazione, nella radice del progetto o nelle variabili d'ambiente. Devono essere facilmente modificabili. NON ESEGUIRE MODIFICHE DI CONFIGURAZIONE MODIFICANDO IL CODICE SORGENTE.
-Se esiste un file di configurazione che dipende dall'ambiente, non deve essere salvato nel repository git (usa .gitignore). Tuttavia, un utente dovrebbe sapere come creare questo file di configurazione, quindi crea un file config.tpl che verrà caricato nel repository.
- Lo sviluppatore dovrebbe commentare le parti interessanti del codice.
- Tutto il codice deve essere scritto in stile inglese (ad esempio, "indice" deve diventare "index"). Il linguaggio utilizzato per scrivere il README e i commenti deve essere l'inglese.

## Suggerimenti per Python 
Se si utilizza Python, si consiglia di usare i seguenti pacchetti: 
* poetry https://python-poetry.org/docs/ per il packaging 
* typer https://typer.tiangolo.com/ per la realizzazione di command-line interfaces.

## Convenzione per i commit 
Per fare commit correttamente utilizzare la seguente convenzione:
```
    build: Build related changes (eg: npm related/ adding external dependencies)
    chore: A code change that external user won't see (eg: change to .gitignore file or .prettierrc file)
    feat: A new feature
    fix: A bug fix
    docs: Documentation related changes
    refactor: A code that neither fix bug nor adds a feature. (eg: You can use this when there is semantic changes like renaming a variable/ function name)
    perf: A code that improves performance
    style: A code that is related to styling
    test: Adding new test or making changes to existing test
```

Seguire la seguente guida: 
https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/

utilizzo 