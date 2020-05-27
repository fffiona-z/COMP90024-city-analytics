
    // author: Group25
    //         Fangfei Zheng 965378 (China)
    //         Jingjiahui Lu 966172 (Melb)
    //         Xi Chen 983241(China)
    //         Haoran Zhang 960374 (China)
    //         Pengnan Zhao 883338(China)
 

function(keys, values, rereduce) {
    if (rereduce) {
        return sum(values);
    } else {
        return values.length;
    }
}
