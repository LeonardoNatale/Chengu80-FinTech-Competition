class factorMap{

	constructor(){

		this.map = new Map([
			["marital_status",new Map([
				[1,"Married"],
				[2,"Widowed"],
				[3,"Divorced"],
				[4,"Separated"],
				[5,"Never married"]
				])],
			["sex",new Map([
				[1,"Male"],
				[2,"Female"]
				])],
			["occupation",new Map([
				[1,"Administrator, manager"],
				[2,"Teacher"],
				[3,"Professional"],
				[4,"Administrative support, including clerical"],
				[5,"Sales, retail"],
				[6,"Sales, business goods and services"],
				[7,"Technician"],
				[8,"Protective service"],
				[9,"Private household service"],
				[10,"Other service"],
				[11,"Machine operator, assembler, inspector"],
				[12,"Transportation operator"],
				[13,"Handler, helper, laborer"],
				[14,"Mechanic, repairer, precision production"],
				[15,"Construction, mining"]
				])],
			["intended_occupation",new Map([
				[1,"Administrator, manager"],
				[2,"Teacher"],
				[3,"Professional"],
				[4,"Administrative support, including clerical"],
				[5,"Sales, retail"],
				[6,"Sales, business goods and services"],
				[7,"Technician"],
				[8,"Protective service"],
				[9,"Private household service"],
				[10,"Other service"],
				[11,"Machine operator, assembler, inspector"],
				[12,"Transportation operator"],
				[13,"Handler, helper, laborer"],
				[14,"Mechanic, repairer, precision production"],
				[15,"Construction, mining"]
				])],
			["education_level",new Map([
				[0,"Never attended school"],
				[10,"First through eighth grade"],
				[11,"Ninth through twelfth grade (no H.S. diploma)"],
				[12,"High school graduate"],
				[13,"Some college, less than college graduate"],
				[14,"Associate's degree (occupational/vocational or academic)"],
				[15,"Bachelor's degree"],
				[16,"Master's degree, (professional/Doctorate degree)*"]
				])],
			["intended_education",new Map([
				[0,"Never attended school"],
				[10,"First through eighth grade"],
				[11,"Ninth through twelfth grade (no H.S. diploma)"],
				[12,"High school graduate"],
				[13,"Some college, less than college graduate"],
				[14,"Associate's degree (occupational/vocational or academic)"],
				[15,"Bachelor's degree"],
				[16,"Master's degree, (professional/Doctorate degree)*"]
				])],
			["house_tenure",new Map([
				[1,"Owned with mortgage"],
				[2,"Owned without mortgage"],
				[4,"Rented"],
				[5,"Occupied without payment of cash rent"],
				[6,"Student housing"]
				])]
			]);
	}

	getValue(factor, key){
		return this.map.get(factor).get(key);
	}

	getValueCode(factor, value){
		var auxMap = this.map.get(factor.toLowerCase());
		var iterator = auxMap[Symbol.iterator]();

		for(let item of iterator){
			if(item[1].toLowerCase() == value.toLowerCase()) return item[0];
		}
		return -1
	}
}