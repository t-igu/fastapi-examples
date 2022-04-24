function syncFetchHandler(response){
    if(!response.ok){
        throw Error(response.statusText);
    }
    return response;
}

function syncFetchError(e){
    console.log(e);
}

syncFetch = async(url, options={}) => {
    return await (
            await fetch(url, options).then(syncFetchHandler).catch(syncFetchError)
        ).json();
}

