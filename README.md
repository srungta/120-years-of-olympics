## Olympics.
> The modern Olympic Games or Olympics are leading international sporting events featuring summer and winter sports competitions in which thousands of athletes from around the world participate in a variety of competitions. The Olympic Games are considered the world's foremost sports competition with more than 200 nations participating. The Olympic Games are held every four years, with the Summer and Winter Games alternating by occurring every four years but two years apart.

This repository contains code to analyze the dataset published on Kaggle at [this link](https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results)

---
#### Repository structure
The structure of the repository is following.
- **README.md**  describes the repository and its contents.
- **visualization/** has code required to index data in an [ElasticSearch](https://www.elastic.co/) index and later use [Kibana](https://www.elastic.co/webinars/getting-started-kibana?elektra=home&storm=sub2) as a visualization tool.
- **scripts/** has code that is required to analyze the data in simple python scripts.
- **notebooks/** has Jupyter notebooks used for analysis of the data.
- **results/** has the result images, summaries and visuals from the analysis.
- **data/** has datasets that is used for analysis. The data files are tracked using `git lfs`. The description of dataset can be found in the README inside this folder.

---
#### Environment setup
- **OS**  
Windows 10/x64
- **Python installation**  
Miniconda installation with conda 4.5.1 + Python 3.6.4
- **ElasticSearch**  
Installation and initialization of ElasticSearch is quite simple.
  + [Download](https://www.elastic.co/start) and unzip Elasticsearch to a folder of your choice.
  + Run bin/elasticsearch (or bin\elasticsearch.bat on Windows).

  > Elasticsearch instance should be running at http://localhost:9200 in your browser if you run with default configuration.

  Keep the terminal open where elastic search is running to be able to keep the instance running.  
  You could also use `nohup` mode to run the instance in the background.
``` json
"version" : {
    "number" : "6.3.1",
    "build_flavor" : "default",
    "build_type" : "zip",
    "build_hash" : "eb782d0",
    "build_date" : "2018-06-29T21:59:26.107521Z",
    "build_snapshot" : false,
    "lucene_version" : "7.3.1",
    "minimum_wire_compatibility_version" : "5.6.0",
    "minimum_index_compatibility_version" : "5.0.0"
  }
```
- **Kibana**  
Installation and initialization is similar to that of Elasticsearch:

  + Download and unzip Kibana.
  + Open `config / Kibana.yml` in an editor.
  + Set elasticsearch.url to point at your Elasticsearch instance.
  + Change the directory to Kibana folder.
  + Run bin/Kibana (or bin\Kibana.bat on Windows)

  > Kibana instance should be running at http://localhost:5601 in your browser if you run with default configuration.

  Keep the terminal open where Kibana was run to be able to keep the instance running.  
  You could also use `nohup` mode to run the instance in the background.

---
#### Summary of discoveries from dataset
Summary of discoveries can be found in the [README.md](./results/README.md) file in ` results/` folder.
