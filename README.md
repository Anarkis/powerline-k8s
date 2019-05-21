# K8s context for powerline-shell

### Why
Usually I work in different kubernetes contexts/namespaces, I need to be aware of which one I'm performing the commands.
I would like to have something like this in my prompt:

`user > **k8s-context** > other info`

[powerline-shell github repo](https://github.com/b-ryan/powerline-shell)

### How
Due to powerline-shell is incredible customizable, only adding a few files you can get it.
I decided to use the kubernetes comand `kubectl config current-context` it will give me isolation about `ENV variables` and other futures changes in Kubernetes client.

#### Output
  - If the kubernetes context is defined we will see something like this: `user > k8s-context > other info`
  - If the kubernetes context is *not* defined we will see this: `user > * > other info`

#### Extending powerline-shell
1. Adding .config folder to your ~/ directory  
  inside you can find `config.json`, which defines all the structure of your prompt  
  Here we add in third segment the path of the python code.

2. The file `k8s-context.py`has to be placed in the same path that we set in the `config.json`

3. Enjoy working with k8s and powerline-shell
