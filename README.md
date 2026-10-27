# CUSTOM NEKO REPO
A collection of NEKO VOID templates for xbps-src
### x86_64 REPO
example

``` 
sudo xbps-install  -S --repository=https://github.com/Neko-Void-Linux/repo-neko/releases/download/stable steam-nk
```

### You can add the repo of neko void with: 

```
echo "repository=https://github.com/Neko-Void-Linux/repo-neko/releases/download/stable" | sudo tee /etc/xbps.d/nekovoid.conf
``` 
### Run on void-packages for compile (goverlay-bin and mangowc-latest)
```
sh -c "cat << EOF >> common/shlibs
libscenefx-0.5.so scenefx-0.5_1
libQt6Pas.so.6 qt6pas-6.2.10_1
libcrypto.so.1.1 libssl1.1-1.1.1w_1
EOF"
```  
### FOR UPDATE OR ADD PACKAGES IN REPO RUN ACTION WORKFLOW  (USE GITHUB MIGRATION PLEASE) 
https://github.com/Neko-Void-Linux/repo-neko/actions/workflows/Migration.yml
