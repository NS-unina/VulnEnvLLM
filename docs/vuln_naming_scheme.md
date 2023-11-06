# OVAL - Open Vulnerability and Assessment Language

***OVAL*** (*Open Vulnerability and Assessment Language*) è un linguaggio standard per la rappresentazione di vulnerabilità e valutazioni di sicurezza. È stato sviluppato da MITRE Corporation e National Institute of Standards and Technology (NIST) per fornire un modo coerente e automatizzato per esprimere le vulnerabilità e le valutazioni di sicurezza.

La struttura di OVAL è composta da tre parti principali:

- **Definition:** la definizione della vulnerabilità o della valutazione di sicurezza
- **Test:** i test che possono essere utilizzati per verificare la presenza della vulnerabilità o per valutare la sicurezza di un sistema
- **Object:** gli oggetti informatici a cui si applicano la vulnerabilità o la valutazione di sicurezza.

## Definition

La definizione di OVAL è un elemento XML che rappresenta una vulnerabilità o una valutazione di sicurezza. La definizione è composta da diversi elementi, tra cui:

- **id:** l'ID univoco della definizione
- **class:** il tipo di definizione, che può essere "vulnerability" (vulnerabilità) o "assessment" (valutazione di sicurezza)
- **summary:** un riepilogo della definizione
- **details:** i dettagli della definizione, tra cui informazioni come CVE, CWE e CVSS

## Test

Il test di OVAL è un elemento XML che rappresenta un test che può essere utilizzato per verificare la presenza della vulnerabilità o per valutare la sicurezza di un sistema. Il test è composto da diversi elementi, tra cui:

- **id:** l'ID univoco del test
- **definition_ref:** il riferimento alla definizione a cui si applica il test
- **object:** l'oggetto informatico a cui si applica il test
- **test_condition:** la condizione che deve essere soddisfatta per verificare la presenza della vulnerabilità o per valutare la sicurezza di un sistema

## Object

L'oggetto di OVAL è un elemento XML che rappresenta un oggetto informatico, come un processo, un file o un servizio. L'oggetto è composto da diversi elementi, tra cui:

- **object_type:** il tipo di oggetto
- **object_id:** l'ID univoco dell'oggetto

### Esempio

Il seguente OVAL rappresenta una vulnerabilità in Microsoft Windows 10 che consente a un utente malintenzionato di eseguire codice arbitrario con privilegi elevati:

```xml
<oval_definitions>
  <definition id="CVE-2023-12345" class="vulnerability">
    <vuln_summary>
      <vuln_id>CVE-2023-12345</vuln_id>
      <vuln_title>Microsoft Windows 10 Elevation of Privilege Vulnerability</vuln_title>
      <vuln_description>A vulnerability in Microsoft Windows 10 could allow an attacker to execute arbitrary code with elevated privileges.</vuln_description>
    </vuln_summary>
    <vuln_details>
      <cve_id>CVE-2023-12345</cve_id>
      <cwe_id>CWE-119</cwe_id>
      <cvss_score>10.0</cvss_score>
      <cvss_vector>AV:L/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H</cvss_vector>
    </vuln_details>
  </definition>
</oval_definitions>
<oval_tests>
  <test id="CVE-2023-12345-test-1" definition_ref="CVE-2023-12345">
    <object object_type="registry" object_id="HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run">
      <test_condition>
        <operator>exists</operator>
        <value>malicious_registry_key</value>
      </test_condition>
    </object>
  </test>
</oval_tests>
```

In questo esempio, la definizione di vulnerabilità rappresenta una vulnerabilità in Microsoft Windows 10 che consente a un utente malintenzionato di eseguire codice arbitrario con privilegi elevati. La vulnerabilità è identificata dall'ID CVE-2023-12345.

Il test di OVAL rappresenta un test che può essere utilizzato per verificare la presenza della vulnerabilità. Il test verifica se esiste una chiave di registro specifica (malicious_registry_key). Se la chiave di registro esiste, il test restituisce un risultato positivo, indicando che la vulnerabilità è presente.

L'oggetto di OVAL rappresenta l'oggetto informatico a cui si applica il test. In questo caso, l'oggetto è una chiave di registro.


# CPE - Common Platform Enumeration
***Common Platform Enumeration*** (*CPE*) è un formato standard per l'identificazione di sistemi, software e pacchetti informatici. È stato sviluppato da MITRE Corporation e National Institute of Standards and Technology (***NIST***) per fornire un modo univoco e coerente per identificare i prodotti informatici.

CPE è basato sullo schema di ***Uniform Resource Identifier*** (*URI*) e utilizza una struttura gerarchica per identificare i prodotti informatici. La struttura di CPE è composta da cinque parti:

Ad esempio, il seguente CPE identifica il sistema operativo Microsoft Windows 10, versione 21H2, con aggiornamento KB5017315 applicato:
- **Vendor:** il produttore del prodotto informatico
- **Product:** il nome del prodotto informatico
- **Version:** la versione del prodotto informatico
- **Update:** gli aggiornamenti applicati al prodotto informatico
- **Edition:** l'edizione del prodotto informatico

Ad esempio, il seguente CPE identifica il sistema operativo Microsoft Windows 10, versione 21H2, con aggiornamento KB5017315 applicato:

`cpe:/o:microsoft:windows:10:21h2:kb5017315`

# Package URL
***Package URL*** (*PURL*) standardizes how software package metadata is represented so that packages can be universally located regardless of what vendor, project, or ecosystem the packages belongs.

A PURL is a valid RFC3986 ASCII string defined URL composed of seven elements. Each of them is separated by a defined character in order to make it easily manipulated by software.

`scheme:type/namespace/name@version?qualifiers#subpath`

The definition for each component is:

- **scheme:** URL scheme compliant constant value of “pkg”. (Required).
- **type:** package type or package protocol such as maven, npm, nuget, gem, pypi, etc. (Required).
- **namespace:** type-specific value to a package prefix such as it’s owner name, groupid, etc. (Optional).
- **name:** name of the package. (Required).
- **version:** package version. (Optional).
- **qualifiers:** extra qualifying data for a package such as an OS, architecture, a distro, etc. (Optional).
- **subpath:** extra subpath within a package, relative to the package root. (Optional).

# Da approfondire
E' possibile utilizzare [OVAL Repo](https://github.com/CISecurity/OVALRepo) che permette di scaricare tutte le definizioni OVAL in un unico file XML, ovviamente è possibile definire dei filtri su date,architettura, famiglia, piattaforma etc.
Una definizione di prova presa da una estrazione della suddetta repo che ci mostra come quasi ogni definizione contiene un riferimento al CVE
```xml
		<definition xmlns="http://oval.mitre.org/XMLSchema/oval-definitions-5" class="patch" id="oval:org.mitre.oval:def:22012" version="18">
		  <metadata>
		    <title>ELSA-2008:0981: ruby security update (Moderate)</title>
		    <affected family="unix">
		      <platform>Oracle Linux 5</platform>
		      <product>ruby</product>
		    </affected>
		    <reference ref_id="ELSA-2008:0981-04" ref_url="http://linux.oracle.com/errata/ELSA-2008-0981.html" source="VENDOR" />
		    <reference ref_id="CVE-2008-4310" ref_url="http://linux.oracle.com/cve/CVE-2008-4310.html" source="CVE" />
		    <description>httputils.rb in WEBrick in Ruby 1.8.1 and 1.8.5, as used in Red Hat Enterprise Linux 4 and 5, allows remote attackers to cause a denial of service (CPU consumption) via a crafted HTTP request.  NOTE: this issue exists because of an incomplete fix for CVE-2008-3656.</description>
		    <oval_repository>
		      <dates>
		        <submitted date="2014-01-13T12:30:04.000-05:00">
		          <contributor organization="Hewlett-Packard">Vinay Naikar</contributor>
		        </submitted>
		        <status_change date="2014-03-18T08:53:34.118-04:00">DRAFT</status_change>
		        <status_change date="2014-04-07T04:02:28.418-04:00">INTERIM</status_change>
		        <status_change date="2014-04-28T04:00:41.993-04:00">ACCEPTED</status_change>
		        <modified comment="EDITED oval:org.mitre.oval:def:22012 - optimisation of Oracle Linux content" date="2014-05-05T18:21:00.458-04:00">
		          <contributor organization="ALTX-SOFT">Maria Mikhno</contributor>
		        </modified>
		        <status_change date="2014-05-05T18:23:10.658-04:00">INTERIM</status_change>
		        <status_change date="2014-05-26T04:00:47.984-04:00">ACCEPTED</status_change>
		      </dates>
		      <status>ACCEPTED</status>
		      <min_schema_version>5.3</min_schema_version>
		    </oval_repository>
		  </metadata>
		  <criteria>
		    <extend_definition comment="Oracle Linux 5.x" definition_ref="oval:org.mitre.oval:def:15459" />
		    <criteria comment="rpm test" operator="OR">
		      <criterion comment="ruby-ri is earlier than 0:1.8.5-5.el5_2.6" test_ref="oval:org.mitre.oval:tst:102731" />
		      <criterion comment="ruby-docs is earlier than 0:1.8.5-5.el5_2.6" test_ref="oval:org.mitre.oval:tst:102729" />
		      <criterion comment="ruby-mode is earlier than 0:1.8.5-5.el5_2.6" test_ref="oval:org.mitre.oval:tst:102546" />
		      <criterion comment="ruby-libs is earlier than 0:1.8.5-5.el5_2.6" test_ref="oval:org.mitre.oval:tst:102432" />
		      <criterion comment="ruby-tcltk is earlier than 0:1.8.5-5.el5_2.6" test_ref="oval:org.mitre.oval:tst:102102" />
		      <criterion comment="ruby-irb is earlier than 0:1.8.5-5.el5_2.6" test_ref="oval:org.mitre.oval:tst:102079" />
		      <criterion comment="ruby-rdoc is earlier than 0:1.8.5-5.el5_2.6" test_ref="oval:org.mitre.oval:tst:102725" />
		      <criterion comment="ruby is earlier than 0:1.8.5-5.el5_2.6" test_ref="oval:org.mitre.oval:tst:102561" />
		      <criterion comment="ruby-devel is earlier than 0:1.8.5-5.el5_2.6" test_ref="oval:org.mitre.oval:tst:102319" />
		    </criteria>
		  </criteria>
		</definition>
```
