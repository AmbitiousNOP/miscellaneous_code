#include <stdio.h>
#include <curl/curl.h>


int main(){
    char http_header[] = "http://www.google.com";

    CURLU *h = curl_url();

    CURLUcode rc = curl_url_set(h, CURLUPART_URL, http_header, 0);
    if (rc){
        printf("Error: could not init url.\n");
        return 1;
    }
    
    char *host = NULL;
    CURLUcode host_code = curl_url_get(h, CURLUPART_HOST, &host, 0);
    if (host_code){
        printf("Error: could not parse URL host.\n");
        return 1;
    }

    char *path = NULL;
    CURLUcode path_code = curl_url_get(h, CURLUPART_PATH, &path, 0);
    if (path_code){
        printf("Error: could not parse URL path.\n");
        return 1;
    }


    printf("Url: %s\n", http_header);
    printf("Host: %s\n", host);
    printf("Path: %s\n", path);
    
    curl_free(path);
    curl_free(host);
    curl_url_cleanup(h);
    


    return 0;
}
