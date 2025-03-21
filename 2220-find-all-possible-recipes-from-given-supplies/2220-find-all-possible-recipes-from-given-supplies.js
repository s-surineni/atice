/**
 * @param {string[]} recipes
 * @param {string[][]} ingredients
 * @param {string[]} supplies
 * @return {string[]}
 */
var findAllRecipes = function (recipes, ingredients, supplies) {
    const supplySet = new Set(supplies);
    const recipeIdx = {}
    for (let i = 0; i < recipes.length; i++) {
        recipeIdx[recipes[i]] = i;
    }
    const dependencyGraph = {};
    const indegree = new Array(recipes.length).fill(0);
    for (let idx = 0; idx < ingredients.length; idx++) {
        for (const anIgredient of ingredients[idx]) {
            if (!supplySet.has(anIgredient)) {
                if (!dependencyGraph[anIgredient]) {
                    dependencyGraph[anIgredient] = [];
                }
                dependencyGraph[anIgredient].push(recipes[idx]);
                indegree[idx] += 1;
            }
        }
    }
    const queue = [];
    for (let i = 0; i < recipes.length; i++) {
        if (indegree[i] === 0) {
            queue.push(recipes[i]);
        }
    }
    const result = [];
    while (queue.length) {
        const recipe = queue.shift();
        result.push(recipe);
        if (dependencyGraph[recipe]) {
            for (const depRecipe of dependencyGraph[recipe]) {
                indegree[recipeIdx[depRecipe]] -= 1;
                if (indegree[recipeIdx[depRecipe]] === 0) {
                    queue.push(depRecipe);
                }
            }
        }
    }
    return result;
};
