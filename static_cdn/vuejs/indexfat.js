new Vue({
    el: '#appfat',
    data: {
        form: {
            first_name: '',
            last_name: '',
            username: '',
            email: '',
            password: '',
            password2: '',
            file: '',
        },
        isSuccess:false,
        error:false,
        messageRes:'',
    },
    delimiters: ["${", "}"],
    mounted(){
    
    },
    methods: {
        handleFileUpload:function(){
            this.form.file = this.$refs.file.files[0];
        },
        onSubmit(evt){
            evt.preventDefault()

            let formData=new FormData()
            formData.append('file', this.form.file)
            formData.append('username', this.form.username)
            formData.append('email', this.form.email)
            formData.append('first_name', this.form.first_name)
            formData.append('last_name', this.form.last_name)
            formData.append('password', this.form.password)
            formData.append('password2', this.form.password2)
    
            axios.defaults.xsrfCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = 'X-CSRFToken'
    
            const path = `http://127.0.0.1:8000/comptes/registerapi`
                    
            axios.post(path, formData,{

                 headers: {
                        // 'Content-Tranfer-Encoding': 'multipart/form-data',
                        'Content-Type': 'multipart/form-data'
                }

                // headers: {
                //     'Content-Type': 'multipart/form-data',
                // }
            })
            .then(response => { 
                // console.log(response) 
                // this.form.first_name = response.data.first_name
                // this.form.last_name = response.data.last_name
                // this.form.username = response.data.username
                // this.form.email = response.data.email  
                // this.form.password = response.data.password  
                // this.form.password2 = response.data.password2  
                // this.form.imageprofi = response.data.imageprofi
                
                // console.log('ok pOST')
                // swal("Merci!", "Votre formulaire contact a ete soumis avec succes!", "success");
                
                console.log(response.data.success) 
                console.log(response.data.message) 

                if(response.data.success == true){
                    this.isSuccess=true
                    this.error=false
                    this.messageRes=response.data.message
                    // console.log('Ok Goog')

                    // window.location = "http://127.0.0.1:8000/comptes/loginvisit/";

                }
                else{
                    this.error=true
                    this.isSuccess=false
                    this.messageRes=response.data.message
                    console.log('Fake connec')
                }


                this.form.first_name = ''
                this.form.last_name = ''
                this.form.username = ''
                this.form.email = ''
                this.form.password = ''
                this.form.password2 = ''
                this.form.file = ''
    
            })
            .catch(error => {
                console.log(error.response.data)
            });
        },
    },
            
});


new Vue({
    el: '#appfatlog',
    data: {
        form: {
            username: '',
            password: '',
    
        },
        isSuccess:false,
        error:false,
        messageRes:'',
    },
    delimiters: ["${", "}"],
    mounted(){
        // this.getContact()
    },
    methods: {
        onsubmitLogin(evt){
            evt.preventDefault()
    
            axios.defaults.xsrfCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = 'X-CSRFToken'
    
            const path = `http://127.0.0.1:8000/comptes/loginapi`
                    
            axios.post(path, this.form)
            .then(response => { 
                console.log(response) 
                this.form.username = response.data.username  
                this.form.password = response.data.password  
                
                // console.log('ok pOST')
                // swal("Merci!", "Votre formulaire contact a ete soumis avec succes!", "success");
                
                console.log(response.data.success) 
                console.log(response.data.message) 

                // console.log('Ok Goog')

                if(response.data.success == true){
                    this.isSuccess=true
                    this.error=false
                    this.messageRes=response.data.message
                    console.log('Ok Goog')

                    window.location = "http://127.0.0.1:8000/comptes/profile/";

                }
                else{
                    this.error=true
                    this.isSuccess=false
                    this.messageRes=response.data.message
                    console.log('Fake connec')
                }

                this.form.username = ''
                this.form.password = ''
    
            })
            .catch(error => {
                console.log(error.response.data)
            });
        },
    },
           
});























